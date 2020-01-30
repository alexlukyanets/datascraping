from ListVacancy import ListVacancy
from UrlSet import UrlSetting
from SmartSearch import SmarSearch

language = 'ru'
inputquery = 'python'
inputcategory = 'IT'
inputscity = 'Харьк'

truecity = SmarSearch.search_city(inputscity)
truecategory = SmarSearch.search_category(inputcategory)

print(truecategory)
all_url = UrlSetting.setting(language, inputquery, truecategory, truecity)
print(all_url)

#text = ListVacancy.next_page(all_url,language)
#print(text)
data = ListVacancy.ListSentence(all_url)
data