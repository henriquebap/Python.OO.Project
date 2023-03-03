url = "https://.bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#url = "    "

#tratamento da Url

#url = url.replace(" ", "")
url = url.strip()

#Validacao da URL:
if url == "":
    raise ValueError("O valor da URL esta vazio")

print(url)

#Separa Base e parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca valores de parametros
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)