from GetCity import GetCity
from GetCategory import GetCategory

class UrlSetting():
    
    @classmethod
    def try_get_city(cls, name):
        
        city = GetCity.both_ua_ru(name)

        if city == "None":
            return ''
        
        return city

    @staticmethod
    def get_url(language, query, myscity, category):
       
        if category == '':
            #Запрос без города по всей стране
            if myscity == '' :
                #print(1)
                all_url = "https://www.work.ua/{}/jobs".format(language) + "-" + query
                return all_url
            
            
            # Запрос с городом с русской и укр локализацией
            elif query != '' and myscity != '' :
                #print(2)
                all_url = "https://www.work.ua/{}".format(language) + '/jobs-'+ myscity + "-" + query
                return all_url
            
            # Без ззапроса с городом
            if query == '':
                #print(3)
                all_url = "https://www.work.ua/{}".format(language)+ '/jobs-'+ myscity
                return all_url
        else:
            #https://www.work.ua/ru/jobs-kharkiv-it-python/?advs=1
            
            # Без ззапроса с городом с русской и укр локализацией с категорией
            if query == '' and myscity != '':
                #print(4)
                all_url = "https://www.work.ua/{}".format(language)+ '/jobs-'+ myscity  + '-'+ category
                return all_url
            
            # Запрос с городом с русской и укр локализацией
            elif query != '' and myscity != '' :
                #print(5)
                all_url = "https://www.work.ua/{}".format(language)+ '/jobs-'+ myscity  + '-'+ category + "-" + query
                return all_url
            
            #Запрос без города по всей стране
            if myscity == ''  and query != '':
                #print(6)
                all_url = "https://www.work.ua/{}/jobs".format(language) + '-'+ category +  "-" + query
                return all_url
            
            if myscity == '' and query == '':
                #print(7)
                all_url = "https://www.work.ua/{}".format(language)+ '/jobs' + '-'+ category
                return all_url

    @classmethod
    def get_category(cls, category):
        data_category = GetCategory.get_category_all(category)
       
        if data_category == "None":
        
            return ''

        return data_category

    @classmethod
    def setting(cls, language, inputquery, inputcategory, truecity):
        myscity= cls.try_get_city(truecity)
        category = cls.get_category(inputcategory)
        all_url = cls.get_url(language, inputquery, myscity, category)

        return all_url