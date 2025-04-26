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
     elif vibor == "Change":
          change()

def allcards():
    message = ""
    for cards_id, cards_info in cards.items():
        message += f"Name: {cards_id}\n" 
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


def change():
        while menu:
            change_characteristic_id = easygui.enterbox("Please write name of card you want to change.")
            if change_characteristic_id not in cards:
                easygui.msgbox("There's no such ID!")
            else:
                break #breaks if user entered ID that doesnt exist in the dictionary


        change_int_or_str = easygui.buttonbox("You want to change the name or stats?", "???", choices= ["Name", "Stats"])
             #asks user what exactly he wants to change. I made it this way because it was easier for me to work separately either with .enterbox or .integerbox
        if change_int_or_str == "Name":
            new_name = easygui.enterbox("Enter new name.")
            cards[change_characteristic_id]= new_name #changes value of name to users input
            menu()
        elif change_int_or_str == "stats": #if user decided to change stats of the card
            while True:
                change_characteristic = easygui.enterbox("Please write what characteristics you want to change.") #asks what kind of stat user wants to change, for example speed, stealth
                if change_characteristic not in cards[change_characteristic_id]:
                     easygui.msgbox("No such characteristic!") #if user entered something that doesnt exist in the dictionary, for example "Power" or "Intellect"
                elif change_characteristic in cards[change_characteristic_id]:
                    new_characteristic = easygui.integerbox("Please enter new characteristic stat") #asking new value of devided characteristics. For example if speed was 1 and user wants make it 25
                    if new_characteristic < 1: #if entered stat doesnt required to minimum amount
                        easygui.msgbox("Too short. Minimum data is - 1.")
                    elif new_characteristic > 25:
                        easygui.msgbox("Too much. Maximum is 25.")
                    else:
                        cards[change_characteristic_id][change_characteristic] = new_characteristic #changes value of key to users value
                        break






def exit():
     exit


starting = easygui.buttonbox("Welcome!", "welcome", choices = ["Start"])
if starting != "Start":
     exit
else:
     menu()
