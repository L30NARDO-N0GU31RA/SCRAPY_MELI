from tasks import ScrapyAnunciosMeli, ScrapyAccountMeli


sua_url_anuncio_mercado_livre = 'https://produto.mercadolivre.com.br/MLB-1598467627-jogo-de-panelas-5-pcs-antiaderente-tampa-de-vidro-_JM?searchVariation=variationID#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-univb-equivalent-offer&reco_client=home_navigation-recommendations&reco_item_pos=4&reco_backend_type=function&reco_id=fae5ced5-6571-464c-ac8e-267c5c9e57e6&c_id=/home/navigation-recommendations/element&c_uid=52f9233d-e5f2-4c7d-b04d-0b3cd42aaff2'
instance = ScrapyAnunciosMeli(sua_url_anuncio_mercado_livre)

instance.get_price()
instance.get_reputacao()
instance.get_seller()
instance.get_view_more()
instance.get_variacoes()
instance.get_title()
instance.get_img()
instance.get_estoque()
dictt = instance.return_dict
print (dictt)
if dictt['retorno']['view_more']:
    instance = ScrapyAccountMeli(dictt['retorno']['view_more'])
    filters = instance.get_filters()

if filters:
    for i in filters:
        print(i)

