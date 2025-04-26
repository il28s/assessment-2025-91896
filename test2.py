import easygui #importing easyGUI

#nested dictionary of all cards
cards = {
    "Stoneling": {
        "Strength": 7, 
        "Speed": 1, 
        "Stealth": 25, 
        "Cunning": 15
    },
    "Vexscream": {
        "Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19
    },
    "Dawnmirage": {
        "Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22
    },
    "Blazegolem": {
        "Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6
    },
    "Websnake": {
        "Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5
    },
    "Moldvine": {
        "Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5
    },
    "Vortexwing": {
        "Strength": 19,
        "Speed": 13, 
        "Stealth": 19, 
        "Cunning": 2
    },
    "Rotthing": {
        "Strength": 16, 
        "Speed": 7, 
        "Stealth": 4, 
        "Cunning": 12
    },
    "Froststep": {
        "Strength": 14, 
        "Speed": 14, 
        "Stealth": 17, 
        "Cunning": 4
    },
    "Wispghoul": {
        "Strength": 17, 
        "Speed": 19, 
        "Stealth": 3, 
        "Cunning": 2
    }
}


def menu():
     vibor = easygui.buttonbox("Select one of the options below.", "Options", choices = ["Cards", "Delete", "Add", "Change", "Search", "Exit", "Menu"])
     if vibor == "Menu":
          menu()
     elif vibor == "Cards":
          allcards()
     elif vibor == "Delete":
          delete()
     elif vibor == "Exit":
          exit()
     elif vibor == "Search":
          search()

def allcards():
    message = ""
    for cards_id, cards_info in cards.items():
        message += f"Card ID: {cards_id}\n" 
        for key, value in cards_info.items():
            message += f" {key}: {value}\n" 
    easygui.msgbox(message, "All cards")
    menu()

def search():
    search = easygui.enterbox('Enter the name of the card for which you want to find information: ')
    if search in cards:
        card = cards[search]
        display = f"Card Name: {search}\n"
        for stat, value in card.items():
            display += f"{stat}: {value}\n"
        easygui.msgbox(display)
    else:
        easygui.msgbox(f"No card found with the name: {search}")

def delete():
        deleting = easygui.enterbox("Please write the ID of the card you want to delete.")
        if deleting not in cards:
            easygui.msgbox("You cant delete something that doesnt exist!")
        else:
            del cards[deleting]
            after_del = easygui.buttonbox(deleting + "" + "is deleted.", choices = ["Menu", "Cards"])
            if after_del == "Menu":
                 menu()
            elif after_del == "Cards":
                 allcards()

def exit():
     exit


starting = easygui.buttonbox("Welcome!", "welcome", choices = ["Start"])
if starting != "Start":
     exit
else:
     menu()
