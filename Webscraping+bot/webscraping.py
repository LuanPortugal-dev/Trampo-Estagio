from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


url = 'https://br.investing.com/currencies/usd-brl'
url2 = 'https://br.investing.com/indices/bovespa'

response = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(response).read()

response2 = Request(url2, headers={"User-Agent": "Mozilla/5.0"})
webpage2 = urlopen(response2).read()

html = BeautifulSoup(webpage, 'html.parser')
html2 = BeautifulSoup(webpage2, 'html.parser')

resultado =  html.select('.pid-2103-pcp')[0].get_text()

resultado2 = html.select('.pid-17920-pcp')[0].get_text()


 

