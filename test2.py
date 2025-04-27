import easygui #importing easyGUI
import sys

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
     elif vibor == "Add":
          add()

def allcards():
    message = ""
    for cards_id, cards_info in cards.items():
        message += f"Name: {cards_id}\n" 
        for key, value in cards_info.items():
            message += f" {key}: {value}\n" 
    easygui.msgbox(message, "All cards")
    menu()

def search():
    search2 = easygui.enterbox('Enter the name of the card for which you want to find information: ')
    if not search2:
         menu()
    while search2:
        if search2 in cards:
            card = cards[search2]
            display = f"Card Name: {search2}\n"
            for stat, value in card.items():
                display += f"{stat}: {value}\n"
            easygui.msgbox(display)
            menu()
            break
        else:
            easygui.msgbox(f"No card found with the name: {search2}")
            search()
            break

def delete():
        deleting = easygui.enterbox("Please write the ID of the card you want to delete.")
        if not deleting:
             menu()
        while True:
            if deleting not in cards:
                easygui.msgbox("You cant delete something that doesnt exist!")
                delete()
                break
            else:
                del cards[deleting]
                after_del = easygui.buttonbox(deleting + "" + "is deleted.", choices = ["Menu", "Cards"])
                if after_del == "Menu":
                    menu()
                elif after_del == "Cards":
                    allcards()
                break
            menu()


def change():
        while menu:
            change_characteristic_id = easygui.enterbox("Please write name of card you want to change.")
            if not change_characteristic_id:
                 easygui.msgbox("Cancelled.")
                 menu()
            elif change_characteristic_id not in cards:
                easygui.msgbox("There's no such ID!")
            else:
                break


        change_int_or_str = easygui.buttonbox("You want to change the name or stats?", "???", choices= ["name", "stats"])
        if change_int_or_str == "name":
            while change_int_or_str:
                 new_name = easygui.enterbox("Enter new name.")
                 if not new_name:
                      easygui.msgbox("Cancelled.")
                      menu()
                 if new_name.isalpha():
                      cards[new_name] = cards.pop(change_characteristic_id)
                      break
                 else:
                      easygui.msgbox("Only letters!")
        
        if change_int_or_str == "stats":
            while True:
                change_characteristic = easygui.enterbox("Please write what characteristics you want to change.") 
                if change_characteristic not in cards[change_characteristic_id]:
                     easygui.msgbox("Canceled.")
                     menu()
                elif change_characteristic in cards[change_characteristic_id]:
                    new_characteristic = easygui.integerbox("Please enter new characteristic stat")
                    if not new_characteristic:
                         easygui.msgbox("Cancelled.")
                         menu()
                    elif new_characteristic < 1: 
                        easygui.msgbox("Too short. Minimum data is - 1.")
                    elif new_characteristic > 25:
                        easygui.msgbox("Too much. Maximum is 25.")
                    else:
                        cards[change_characteristic_id][change_characteristic] = new_characteristic 
                        menu()



def add():
    while True:
        namecard = easygui.enterbox("Please write the NAME of your card")
        if namecard is None:
            easygui.msgbox("Cancelled.")
            menu()
            break
        elif not namecard:
             easygui.msgbox("Enter the name.")
             continue
        elif not namecard.isalpha():
            easygui.msgbox("Only LETTERS!")
            continue
        elif len(namecard) > 25:
            easygui.msgbox('Maximum characters in name is 25')
            continue
        elif namecard in cards:
            easygui.msgbox('This ID alredy in the cards! Try another one')
            continue
        cards[namecard] = {}
        break
             
        
        
        


def exit():
     sys.exit()


starting = easygui.buttonbox("Welcome!", "welcome", choices = ["Start"])
if not starting:
     exit()
else:
     menu()
