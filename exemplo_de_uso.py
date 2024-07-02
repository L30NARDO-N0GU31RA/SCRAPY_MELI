from tasks import ScrapyAnunciosMeli, ScrapyAccountMeli


sua_url_anuncio_mercado_livre = 'https://produto.mercadolivre.com.br/MLB-4107271844-conjunto-panelas-antiaderente-10-pecas-teflon-varias-cores-_JM?searchVariation=variationID#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-univb-equivalent-offer&reco_client=home_navigation-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=3b546e2d-462f-4ddf-89ed-57e900e8a45b&c_id=/home/navigation-recommendations/element&c_uid=50262b28-57c0-4266-9ab7-5db2466fcca5'
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
    for index, value in enumerate(filters, start=1):
        print(f'{index}. {value['title']}')
    filtro = int(input('Digite o número correspondente ao filtro'))
    filtro = filters[filtro-1]
    for index, value in enumerate(filtro['subfilters'], start=1):
        print(f'{index}. {value['name']} {value['quantity']}')
    filtro_cat = int(input('Digite o número correspondente ao filtro'))
    filtro = filtro['subfilters'][filtro_cat-1]
    instance.filter = filtro
    instance.apply_filter()
    instance.get_anuncios()