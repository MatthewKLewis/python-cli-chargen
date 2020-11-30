# Window Functions
import PySimpleGUI as sg

# Py GUI Settingss
sg.theme('DarkAmber')

# CREATE WINDOWS
def createTopWindow():
    topLayout = [ [sg.Button('Create'), sg.Button(' View ')],
                [sg.Button('Modify'), sg.Button('Delete')] ]
    return sg.Window('CharGen', topLayout, font="monospace")

def createInitialInfoWindow():
    nameLayout = [
        [sg.Text('Name'), sg.InputText('')], 
        [sg.Text('Age '), sg.Slider((18,80), orientation="horizontal")],
        [sg.Text('Bio '), sg.InputText('')],
        [sg.Text('Race'), sg.Radio("Human", 1), sg.Radio("Android", 1), sg.Radio("New-type", 1)], 
        [sg.Button('Submit'), sg.Cancel()]]
    return sg.Window('CharGen', nameLayout, font="monospace")

def createHomeworldWindow():
    hwLayout = [
        [sg.Text('Home World'), sg.Radio("Earth", 1), sg.Radio("Sidespace", 1), sg.Radio("Mars colony", 1)], 
        [sg.Text('Region'), sg.InputText('')], 
        [sg.Button('Submit'), sg.Cancel()]]
    return sg.Window('CharGen', hwLayout, font="monospace")

# VIEW WINDOWS
def createCharacterViewerWindow(array):
    # Print length of the old character array
    print('Characters in Query:', len(array))

    # Set up the layout of the window with just a header
    cvLayout = [
        [sg.Text('Character')]]

    # For each character in the array, add a line with the character's name
    for character in array:
        cvLayout.append([sg.Text(character.name)])
        cvLayout.append([sg.Text(character.bio)])
        cvLayout.append([sg.Text(character.race)])
        cvLayout.append([sg.Text(character.homeworld)])
        cvLayout.append([sg.Text(' ')])

    return sg.Window('Character Viewer', cvLayout, font="monospace")