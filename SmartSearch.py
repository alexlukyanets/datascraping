from fuzzywuzzy import fuzz

class SmarSearch():

    @staticmethod
    def readcity():
        
        with open('allcity.csv') as f:
            cities = f.read()
            return cities

    @classmethod
    def search_city(cls, inputscity):

        myread = cls.readcity()
        p = myread.split('\n')

        max_procent = 0
        for item in p:
            procent = fuzz.token_set_ratio(item, inputscity)

            if procent > max_procent:
                max_procent = procent
                maxcity = item

        if max_procent == 0:
            return inputscity
        else:
            return maxcity


    @staticmethod
    def readcategory():

        with open('all_categoyy.csv') as f:
            category = f.read()
            return category


    @classmethod
    def search_category(cls,inputcategory):

        myread = cls.readcategory()
        p = myread.split('\n')

        max_procent = 0

        for item in p:
            procent = fuzz.token_set_ratio(item, inputcategory)
            if procent > max_procent:
                max_procent = procent
                maxcat = item

        if max_procent == 0:
            return inputcategory
        else:
            return maxcat