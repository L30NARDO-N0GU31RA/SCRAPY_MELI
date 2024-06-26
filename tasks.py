import requests
from unidecode import unidecode
from bs4 import BeautifulSoup
from typing import Optional, List, Dict

class ScrapyAnunciosMeli:
    def __init__(self, url: str) -> None:
        """
        Função INIT que inicia todas as variaveis para que o código funcione.


        Args:
            - url (str): Precisa de uma URL válida de um anúncio do Mercado Livre

        Finally:
            - chama a função get_anuncio
        """
        self.url = url
        self.soup: Optional[BeautifulSoup] = False
        self.img: Optional[str] = None
        self.title: Optional[str] = None
        self.price: Optional[str] = None
        self.estoque: Optional[str] = None
        self.variacoes: Optional[List[str]] = None
        self.seller: Optional[str] = None
        self.reputacao: Optional[str] = None
        self.view_more: Optional[str] = None
        self.return_dict: Dict[str, Dict[str, Optional[str]]] = {'status': '200', 'retorno': {}}
        self.get_anuncio()
    
    def get_anuncio(self) -> None:
        """
        Faz a requisição para a URL informada na def INIT
        """
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        if 'mercadolivre.com.br' in self.url:
            response = self.session.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.content, 'html.parser')
            else:
                self.return_dict['status'] = str(response.status_code)
                print(f"Erro na requisição: {response.status_code}")
        else:
            self.return_dict['status'] = 'Informe um link válido do Mercado Livre'

    def extract_text(self, selector: str) -> Optional[str]:
        """
        Função para extrair o texto dentro de um elemento da página

        Args:
            - selector (str): O elemento CSS SELECTOR extraido da página
        """
        if not self.soup:
            print("Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro.")
            return None
        
        element = self.soup.select_one(selector)
        return element.text.strip() if element else None

    def format_estoque(self, estoque: str):
        """
        Função para formatar o texto de estoque que é extraido do site.
        Exemplo de uso:
        (10 disponível)
        será formatado para:
        10

        Args:
        - estoque (str): texto extraido do site

        return:
        - estoque_format (str): texto formatado
        """

        estoque_format = estoque.replace('(', '')
        estoque_format = estoque_format.replace(' disponíveis', '')
        estoque_format = estoque_format.replace(')', '')
        return estoque_format

    def get_reputacao(self) -> None:
        """Extract seller's reputation."""
        self.reputacao = self.extract_text('#reviews_capability_v3 > div > section > div > div:nth-child(1) > article > div > div.ui-review-capability__rating > div:nth-child(1) > p')
        self.return_dict['retorno']['reputacao'] = self.reputacao if self.reputacao else "Elemento de reputação não encontrado."

    def get_price(self) -> None:
        """Extract product price."""
        self.price = self.extract_text('#price > div > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line > span > span')
        self.return_dict['retorno']['price'] = self.price if self.price else 'O elemento de preço não foi encontrado.'

    def get_seller(self) -> None:
        """Extract seller's name."""
        self.seller = self.extract_text('#seller_data > div > div:nth-child(1) > div > div > div.ui-seller-data-header__main-info-container > div > div > span')
        self.return_dict['retorno']['seller'] = self.seller if self.seller else 'O elemento de vendedor não foi encontrado.'

    def get_view_more(self) -> None:
        """Extract link to view more products from the seller."""
        if not self.soup:
            print('Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro.')
            return
        
        view_more_element = self.soup.select_one('#seller_data > div > div:nth-child(3) > div > a')
        self.view_more = view_more_element.get('href') if view_more_element else None
        self.return_dict['retorno']['view_more'] = self.view_more if self.view_more else 'Elemento não encontrado.'

    def get_variacoes(self) -> None:
        """Extract product variations."""
        if not self.soup:
            print('Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro.')
            return

        variacoes_elements = self.soup.select('.ui-pdp-variations__picker-default-container a[title]')
        self.variacoes = [unidecode(variacao.get('title')) for variacao in variacoes_elements if variacao.get('title')]
        self.return_dict['retorno']['variacoes'] = self.variacoes if self.variacoes else 'O produto não tem variações.'

    def get_title(self) -> None:
        if not self.soup:
            print('Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro.')
            return
        """Extract product title."""
        self.title = self.extract_text('#header > div > div.ui-pdp-header__title-container > h1')
        self.return_dict['retorno']['title'] = self.title if self.title else 'Elemento não encontrado.'

    def get_img(self) -> None:
        if not self.soup:
            print('Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro.')
            return
        self.img_element = self.soup.select_one('#gallery > div > div.ui-pdp-gallery__column > span:nth-child(3) > figure > img')
        self.img = self.img_element.get('src') if self.img_element else None
        self.return_dict['retorno']['img'] = self.img if self.img else 'Elemento não encontrado.'

    def get_estoque(self) -> None:
        if not self.soup:
            print('Soup não está inicializado. Certifique-se de chamar get_anuncio() primeiro')
            return
        self.estoque = self.extract_text('#quantity-selector > span > span.ui-pdp-buybox__quantity__available')
        self.return_dict['retorno']['estoque'] = self.format_estoque(estoque=self.estoque)

class ScrapyAccountMeli:
    def __init__(self, url):
        self.url = url
        self.soup: Optional[BeautifulSoup] = False
        self.return_dict: Dict[str, Dict[str, Optional[str]]] = {'status': '200', 'retorno': {}}
        self.filter_dict: Dict[str, Optional[str]] = {}

        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.get_account()

    def get_account(self):
        if 'mercadolivre.com.br' in self.url:
            response = self.session.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.content, 'html.parser')
                element_view_more = self.soup.select_one('#root-app > div.home.home--seller.home--with-padding-bottom.home--os-name__windows > div > div > div:nth-child(2) > div > div > div.ui-recos-carousel-wrapper__header > a')
                if element_view_more:
                    link = element_view_more.get('href')
                    response = self.session.get(link, headers=self.headers)
                    if response.status_code == 200:
                        self.soup = BeautifulSoup(response.content, 'html.parser')
                else:
                    pass
            else:
                self.return_dict['status'] = str(response.status_code)
                print(f"Erro na requisição: {response.status_code}")
        else:
            self.return_dict['status'] = 'Informe um link válido do Mercado Livre'

    def get_filters(self):
        if not self.soup:
            print("HTML content is not loaded.")
            return

        # Seleciona todos os grupos de filtros
        filter_groups = self.soup.select(
            '#root-app > div > div.ui-search-main.ui-search-main--without-header.ui-search-main--only-products > aside > section.ui-search-filter-groups > div.ui-search-filter-dl'
        )

        # Verifica quantos grupos de filtros foram encontrados
        print(f"Number of filter groups found: {len(filter_groups)}")

        filters_data = []

        if filter_groups:
            for group in filter_groups:
                title = group.select_one('h3')
                
                # Verifica se o título foi encontrado
                if title:
                    filter_title = title.text.strip()
                    print(f"Filter group title: {filter_title}")

                    # Seleciona todos os subfiltros dentro do grupo
                    subfilters = group.select('ul > li.ui-search-filter-container > a')

                    subfilter_data = []
                    for subfilter in subfilters:
                        subfilter_name = subfilter.select_one('span.ui-search-filter-name')
                        subfilter_qty = subfilter.select_one('span.ui-search-filter-results-qty')

                        if subfilter_name and subfilter_qty:
                            subfilter_data.append({
                                'name': subfilter_name.text.strip(),
                                'quantity': subfilter_qty.text.strip()
                            })
                    
                    filters_data.append({
                        'title': filter_title,
                        'subfilters': subfilter_data
                    })
                else:
                    print("No title found in this filter group")
        
        return filters_data
    