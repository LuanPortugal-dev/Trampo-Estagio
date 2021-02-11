import requests
import json
import urllib3


# envia uma solicitação GET para o url especificado e pega os dados
r = requests.get('https://api.github.com/users/LuanPortugal-dev')
url_base = 'https://bratestedd.free.beeceptor.com'

headers = {
    "content-length": "524920",
    "User-Agent": "python-requests/2.25.1",
    "accept-encoding": "gzip, deflate",
    "accept": "*/*"
    } 



# MÉTODO PARA ENVIAR DADOS PAR AO SERVIDOR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
req_post = requests.post(url_base, r)



# MÉTODO QUE DELETA ALGO DA URL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#req_del = requests.delete(url_base, headers=headers)



# MÉTODO UTILIZADO PARA TRANSPORTAR DADOS E ARMAZENÁ-LOS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
#req_put = requests.put(url_base)



# HEAD SÃO FEITAS PARA QUANDO VC N PRECISA DO CONTEUDO DO ARQUIVO, APENAS O STATUS_CODE OU O CABEÇALHO!!!!!!!!!!!!!!!
#req_head = requests.head('https://www.w3schools.com/python/demopage.php')
#print(req_head.headers)



# VERIFICA QUAIS VERBOS ESTÃO DISPONÍVEIS PARA USAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#verbs = requests.options('https://bratestedd.free.beeceptor.com')
#print (verbs.headers)
