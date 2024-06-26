from tasks import ScrapyAnunciosMeli


sua_url_anuncio_mercado_livre = 'https://produto.mercadolivre.com.br/MLB-2815611908-kit-6-camisetas-masculinas-lisa-basica-100-algodo-premium-_JM#is_advertising=true&position=12&search_layout=grid&type=pad&tracking_id=5d1de472-a58d-437f-837b-a21b68d3953a&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=12&ad_click_id=ZjdhOTNlMDEtOTE1Ni00ZjEyLWJlNTItMTg5NGU0NTY2ODQz'
instance = ScrapyAnunciosMeli(sua_url_anuncio_mercado_livre)

instance.get_price()
instance.get_reputacao()
instance.get_seller()
instance.get_view_more()
instance.get_variacoes()
instance.get_title()
print(instance.return_dict)