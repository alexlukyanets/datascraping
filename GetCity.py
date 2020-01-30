from peewee import *

db = PostgresqlDatabase('project_db', user='postgres', password='wise2012A', host='localhost', port=5432)
db.connect()   
    
class GetCity():
       
    @staticmethod
    def both_ua_ru(qcity):
        try:
            city = Both_ua_ru.get(Both_ua_ru.city == qcity)
            return city.url
        except:
            note = 'None'
            return note

class Both_ua_ru(Model):
    city = CharField()
    region = CharField()
    number = CharField()
    url = TextField()
    language = CharField()

    class Meta:
        database = db
