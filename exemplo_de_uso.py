from tasks import ScrapyAnunciosMeli, ScrapyAccountMeli


sua_url_anuncio_mercado_livre = 'https://produto.mercadolivre.com.br/MLB-4107271844-conjunto-panelas-antiaderente-10-pecas-teflon-varias-cores-_JM#position=5&search_layout=grid&type=item&tracking_id=3023dbd0-633b-4617-8f17-ea4e88476ff7'
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

