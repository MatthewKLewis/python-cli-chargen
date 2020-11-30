import os, sys, random, datetime
import PySimpleGUI as sg
from peewee import *
from pyguiwrapper import *

# Some environmental variable bug is solved with...
os.environ.__setitem__('DISPLAY', ':0.0')

# connect to database
db = PostgresqlDatabase('characters', user='postgres', password='newPassword', host='localhost', port=5432)
db.connect()
print('Connected to Database')

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

def safeSave(databaseEntry):
    try:
        databaseEntry.save()
        print('entry saved!')
    except:
        print("entry failed to save")

# Pull info from Database
characterQuery = Character.select()

# Create temporary container for new characters
newCharArray = []

# UI Loop
while True:
    #top level control flow
    topWindow = createTopWindow()
    event, values = topWindow.read()

    # if the user closes the top window
    if event == sg.WIN_CLOSED:
        break # goes to window.close()

    if event == 'Create':
        print('create')
        topWindow.close()
        initialInfoWindow = createInitialInfoWindow()
        initialInfoEvent , initialInfo = initialInfoWindow.read()
        if initialInfoEvent == 'Submit':
            initialInfoWindow.close()
            homeworldWindow = createHomeworldWindow()
            homeworldEvent, homeworldInfo = homeworldWindow.read()
            if homeworldEvent == 'Submit':
                homeworldWindow.close()
                # First Window Info
                newCharArray.append(initialInfo[0]) #Name
                newCharArray.append(initialInfo[1]) #Age
                newCharArray.append(initialInfo[2]) #Bio
                if initialInfo[3]:  newCharArray.append('Human') #IF TRUE append Human
                if initialInfo[4]:  newCharArray.append('Android')
                if initialInfo[5]:  newCharArray.append('New-type')
                # Second Window Info
                if homeworldInfo[0]: newCharArray.append('Earth')
                if homeworldInfo[1]: newCharArray.append('Sidespace')
                if homeworldInfo[2]: newCharArray.append('Mars')
                newCharArray.append(homeworldInfo[3]) #Region
                print(newCharArray)
                tempDatabaseEntry = Character(
                    name=newCharArray[0],
                    age=newCharArray[1],
                    bio=newCharArray[2],
                    race=newCharArray[3],
                    homeworld=newCharArray[4],
                    region=newCharArray[5]
                    )
                safeSave(tempDatabaseEntry)
                pass

    if event == ' View ':
        print('view')
        topWindow.close()
        characterViewerWindow = createCharacterViewerWindow(characterQuery)
        ccvEvent , cvInfo = characterViewerWindow.read()

    if event == 'Modify': 
        print('modify')
        topWindow.close()
        characterViewerWindow = createCharacterViewerWindow(characterQuery)
        ccvEvent , cvInfo = characterViewerWindow.read()

    if event == 'Delete': 
        print('delete')
        topWindow.close()
        characterViewerWindow = createCharacterViewerWindow(characterQuery)
        ccvEvent , cvInfo = characterViewerWindow.read()

# topWindow.close()
