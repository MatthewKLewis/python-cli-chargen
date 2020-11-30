import os, sys, datetime
from peewee import *

# Some environmental variable bug is solved with...
os.environ.__setitem__('DISPLAY', ':0.0')

db = PostgresqlDatabase('characters', user='postgres', password='newPassword', host='localhost', port=5432)
db.connect()
print('Connected to Database')

# Safe Save Wrapper:
def safeSave(databaseEntry):
    try:
        databaseEntry.save()
        print('entry saved!')
    except:
        print("entry failed to save")

# Schema -------------------------------------------RUN WHEN DONE
class BaseModel(Model):
    class Meta:
        database = db

class Character(BaseModel):
    name = CharField(unique=True)
    bio = TextField()
    age = IntegerField()
    race = CharField()
    homeworld = CharField()
    region = CharField()
    createdDate: DateTimeField(default=datetime.datetime.now)
    # etc etc

db.create_tables([Character])

milo = Character(name='Milo', bio='The Halfling Thief', age=49, race='Halfling', homeworld='Middle Earth', region='Hobbiton')
bruno = Character(name='Bruno', bio='The Halfling Warrior', age=59, race='Halfling', homeworld='Middle Earth', region='The Shire')
mike = Character(name='Mike', bio='The Halfling Wizard', age=69, race='Halfling', homeworld='Middle Earth', region='The Shire')

safeSave(milo)
safeSave(bruno)
safeSave(mike)

print('Done!')