# Scrapy Anúncios Mercado Livre

Este é um projeto de scraping para extrair informações de anúncios do Mercado Livre. O objetivo deste projeto é capturar detalhes como título, preço, variações, vendedor, reputação do vendedor e link para ver mais produtos do vendedor a partir de uma URL específica de um produto no Mercado Livre.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas listadas no `requirements.txt`

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/L30NARDO-N0GU31RA/scrapy-anuncios-meli.git
    cd scrapy-anuncios-meli
    ```

2. Crie e ative um ambiente virtual:

    No Windows:
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

    No macOS/Linux:
    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Edite o arquivo `exemplo_de_uso.py` e substitua a URL do produto pelo anúncio desejado no Mercado Livre.
2. Execute o script:

    ```bash
    python exemplo_de_uso.py
    ```

## Estrutura do Projeto

```plaintext
scrapy-anuncios-meli/
│
├── env/                        # Ambiente virtual (não incluído no repositório)
├── requirements.txt            # Dependências do projeto
├── tasks.py                    # Script principal
├── exemplo_de_uso.py           # Script para testes
└── README.md                   # Este arquivo


## Contribuições

Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request com suas melhorias. Todas as contribuições são bem-vindas!
