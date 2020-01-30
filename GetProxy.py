import requests
from bs4 import BeautifulSoup
from random import choice

class GetProxy():
    
    @staticmethod
    def get_proxy(https):
        
        html = requests.get('https://free-proxy-list.net/').text
        soup = BeautifulSoup(html, 'lxml')

        trs = soup.find('table', id='proxylisttable').find_all('tr')[1:30]

        proxies = []

        for tr in trs:
            tds = tr.find_all('td')
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            schema= tds[6].text.strip()
            if schema != 'https':
                schema ='http'
                proxy = {'schema': schema, 'address': ip + ':' + port}
                proxies.append(proxy) 

        return choice(proxies)
        

    @classmethod 
    def get_proxy_page(cls):

        https = False

        p = cls.get_proxy(https) 
        proxy = { p['schema']: p['address']  }
      
        return proxy
    