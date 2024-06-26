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
        self.soup: Optional[BeautifulSoup] = None
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

        response = self.session.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            self.return_dict['status'] = str(response.status_code)
            print(f"Erro na requisição: {response.status_code}")

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
        """Extract product title."""
        self.title = self.extract_text('#header > div > div.ui-pdp-header__title-container > h1')
        self.return_dict['retorno']['title'] = self.title if self.title else 'Elemento não encontrado.'

instance = ScrapyAnunciosMeli('https://produto.mercadolivre.com.br/MLB-1376105143-jogo-de-panelas-antiaderente-cereja-8-pcs-c-tampa-de-vidro-_JM#polycard_client=recommendations_vip-pads&reco_backend=vip-pads-star-plus-odin_marketplace&reco_client=vip-pads&reco_item_pos=1&reco_backend_type=low_level&reco_id=39eb45b2-1a9c-4874-a052-77dbf1ae6abb&is_advertising=true&ad_domain=VIPCORE_RECOMMENDED&ad_position=2&ad_click_id=NzJiNDBmYTgtYjkwZS00YzViLTkwODktYWFmMWFiZWZmOTk3')

instance.get_price()
instance.get_reputacao()
instance.get_seller()
instance.get_view_more()
instance.get_variacoes()
instance.get_title()
print(instance.return_dict)