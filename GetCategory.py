from peewee import *

db = PostgresqlDatabase('project_db', user='postgres', password='wise2012A', host='localhost', port=5432)
db.connect()   

    
class GetCategory():
    @staticmethod
    def get_category_all(qcategory):
        #print(1)
        try:
            category = All_category.get(All_category.name == qcategory)
            return category.url
        except:
            note = 'None'
            return note
    
        
class All_category(Model):
    name = CharField()
    url = TextField()
    
    class Meta:
        database = db
    