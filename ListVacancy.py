import requests
from bs4 import BeautifulSoup
from GetProxy import GetProxy

class ListVacancy():

    @classmethod
    def next_page(cls, url, language):
    
        proxy = GetProxy.get_proxy_page()
        r = requests.get(url, proxies=proxy, timeout=5)
        soup = BeautifulSoup(r.text,'lxml')
        try:
            next_link = soup.find('ul', class_ = 'pagination hidden-xs').find('li', class_= 'active').find_next_sibling().find('a').get('href')
            return "https://www.work.ua/ua" + next_link if language == 'ua' else "https://www.work.ua" + next_link
        except:
            return ""
        
    
    @staticmethod
    def GetCity(data):  
            
        try:
            city = data.find('span', class_= 'label-agency').find_next_sibling().find_next_sibling().text.strip()

        except:

            try:
                city = data.find('span', class_= 'label-vip').find_next_sibling().find_next_sibling().text.strip()

            except:
                try:
                    city = data.find('span', class_= 'nowrap').find_next_sibling().text.strip()

                except:

                    try:
                        city = data.find('span').find_next_sibling().find_next_sibling().text.strip()


                    except:
                        city = "None city"

        return city

    @classmethod             
    def ListSentence(cls,url):

        proxy = GetProxy.get_proxy_page()
        
        r = requests.get(url, proxies=proxy, timeout=5)
        
        soup = BeautifulSoup(r.text,'lxml')
        
        
        if soup.findAll('div', class_ = 'card card-hover card-visited wordwrap job-link js-hot-block') == []:
            all_sentence = soup.findAll('div', class_ = 'card card-hover card-visited wordwrap job-link')
        else:
            all_sentence = soup.findAll('div', class_ = 'card card-hover card-visited wordwrap job-link js-hot-block')
    
    
        datadict = []
        
        for item in all_sentence:
            dict = {}
            try:
                title = item.find('h2').text.strip()
            except:
                title = ''
            
            
            try:
                salary = item.find('h2').find_next_sibling().find('b').text.strip()
                salary = salary.replace('\xa0', ' ')
                salary = salary.replace('\u2009', ' ')
                salary = salary.replace('\u202f', ' ')

            except:
                salary = ''
            
            
            
            try:
                mini_descript = item.find('span', 'text-muted').find_next_sibling().text.strip()
                mini_descript = mini_descript.replace('\xa0', ' ')
                mini_descript = mini_descript.replace('\xa0', ' ')
                mini_descript = mini_descript.replace('\u2009', ' ')
                mini_descript = mini_descript.replace('\u202f', ' ')
            except:
                mini_descript = 'None mini_descript'
            
        
            
            try:
                company = item.find('div', class_= 'add-top-xs').find('b').text.strip()
            except:
                company = 'None company'
            
            
            try:
                data = item.find('div',class_= 'add-top-xs' )
                city = cls.GetCity(data)
            except:
                city = "Nonecity"
        
            
            
            try:
                data = item.find('span', class_= 'label-agency').text.strip()
                agency = data
            except:
                agency = "None agency"
            
            
            try:
                distance =  item.find('span', class_= 'distance-block unclickable-inner-block border-dashed-grey').find('span').text.strip()
                distance = distance.replace('\xa0', ' ')
                distance = distance.replace('\xa0', ' ')
                distance = distance.replace('\u2009', ' ')
                distance = distance.replace('\u202f', ' ')
            except:
                distance = 'Non distance'
            
            
            try:
                reqdesc = item.find('p', class_= "overflow text-muted add-top-sm add-bottom").text.strip()
                reqdesc = reqdesc.replace('\n', '')
                reqdesc = reqdesc.replace('\xa0', ' ')
                reqdesc = reqdesc.replace("""…\u2060""", "...")
                reqdesc = reqdesc.split('.                            ')
                requirements = reqdesc[0]
                discription = reqdesc[1]
            except:
                requirements = 'None'
            
            try:
                url = item.find('h2').find('a').get('href')
                url = 'https://www.work.ua' + url
            except:
                url = 'Non url'
            
            dict = {'title': title,
                    'salary': salary,
                    'mini_descript': mini_descript,
                    'company': company,
                    'city': city,
                    'agency': agency,
                    'distance': distance,
                    'requirements': requirements,
                    'discription': discription,
                    'url': url}
            
            datadict.append(dict)
        
        return datadict



    
    

