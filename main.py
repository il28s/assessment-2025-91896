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


def menu(): #this function launches easygui buttonbox which is basically a main menu/navigation page of the program
     vibor = easygui.buttonbox("Select one of the options below.", "Options", choices = ["Cards", "Delete", "Add", "Change", "Search", "Exit", "Menu"]) #displays a Easy Gui User interface with 6 buttons. Each button calls specific function
     if vibor == "Menu":
          menu() #this button calls menu function
     elif vibor == "Cards":
          allcards() #calls allcards function and shows all the cards 
     elif vibor == "Delete":
          delete() #calls delete function, needs to delete the whole card
     elif vibor == "Exit":
          exit() #calls an exit button
     elif vibor == "Search":
          search() #calls searching function
     elif vibor == "Change":
          change() #calls a change function
     elif vibor == "Add":
          add() #calls add function

def allcards(): #function that shows information of all cards in dictionary
    message = "" #empty text where will be add all the infomation about  cards
    for cards_id, cards_info in cards.items(): #go through all cards name and info in the dictionary
        message += f"Name: {cards_id}\n" #adds cards name into the message 
        for key, value in cards_info.items(): #goes through key and value for each card 
            message += f" {key}: {value}\n" #adds key and value for each card into the message
    easygui.msgbox(message, "All cards") #shows all collected information about all cards in easygui messagebox
    menu() #calls the menu functiom when user presses the "OK" button in previous messagebox

def search(): #function that search information of a specific card that user wants to find 
    while True: #while loop so it keeps asking until the user finds a card or cancels 
        search2 = easygui.enterbox('Enter the name of the card for which you want to find information: ') #asks the user ti type the card name
        if search2 is None: #if the user presser cancel
                easygui.msgbox("Cancelled.") #shows the messagebox "cancelled."
                menu() #calls the menu function
                break #stops the loop
        elif not search2: #if the user didnt type anything
            easygui.msgbox("Enter the name.") #tells the user enter the name
            continue #restarts the loop
        elif search2.title() not in cards: #if the name user entered is not exist in the dictionary
            easygui.msgbox(f"No card found with the name: {search2.title()}") #tells the user card is not found
            continue #restarts the loop
        else: #if the card exist
                    card = cards[search2.title()] #all information of the cards
                    display = f"Card Name: {search2}\n" #the name of the card user entered
                    for stat, value in card.items(): #goes through all the stats in specific card
                        display += f"{stat}: {value}\n" #put all collected information about entered card to the display message
                    easygui.msgbox(display) #siaplays all information about the card
                    menu() #calls menu function
                    break #breaks the loop
                
            
                    

def delete(): #calls delete function
        while True:
            deleting = easygui.enterbox("Please write the name of the card you want to delete.") #asks for a name of the card user wants to delete
            if deleting is None: 
                easygui.msgbox("Cancelled.") #if user presses the "cancel" button the loops breaks and it goes to the main menu
                menu()
                break
            elif not deleting: 
                easygui.msgbox("Enter the name.") #is user didnt entered anything or just pressed enter then loop is restarts
                continue
            
            elif deleting.title() not in cards: 
                easygui.msgbox("You cant delete something that doesnt exist!") #if the name is not in the dictionary
                continue
            else:
                del cards[deleting.title()] #if the name in the dictionary program deletes the card by using "del"
            after_del = easygui.buttonbox(deleting + "" + "is deleted.", choices = ["Menu", "Cards"]) #tells user that card is deleted
            if after_del == "Menu":
                menu() #if user presses menu button it goes to the menu
            elif after_del == "Cards":
                allcards() #is user presses cards button it goes to the allcards (calling allcards function)
                break
            


def change():
        while True:
            change_characteristic_id = easygui.enterbox("Please write name of card you want to change.") #asks for the name of card he wants to change
            if change_characteristic_id is None:
                easygui.msgbox("Cancelled.") #if user presses the "cancel" button the loops breaks and it goes to the main menu
                menu()
                break
            elif not change_characteristic_id:
                 easygui.msgbox("Enter the name.") #if user didnt entered anything or just pressed enter then loop is restarts
                 continue
            elif change_characteristic_id.title() not in cards:
                easygui.msgbox("There's no such ID!")  #if the name is not in the dictionary
                continue
            else:
                change_int_or_str = easygui.buttonbox("You want to change the name or stats?", "???", choices= ["name", "stats"]) #program finds the name but asks what exactly he wants to change
                if change_int_or_str == "name":
                    while True:
                        new_name = easygui.enterbox("Enter new name.") #if user decided to change a name the programm asks for the name of the card user wants to change
                        if new_name is None:
                            easygui.msgbox("Cancelled.") #if user presses the "cancel" button the loops breaks and it goes to the main menu
                            menu()
                            break
                        elif not new_name:
                            easygui.msgbox("Enter the name.")  #if user didnt entered anything or just pressed enter then loop is restarts
                            continue
                        elif not new_name.isalpha():
                            easygui.msgbox("Only letters!") #isalpha() checks if there is any symbols besides the letters
                            continue
                        else:
                            cards[new_name.title()] = cards.pop(change_characteristic_id.title()) #change the old name of the old card to the new name
                            easygui.msgbox("The card has been changed.")
                            menu()
                            break
        
                if change_int_or_str == "stats":
                    while True:
                        change_characteristic = easygui.enterbox("Please write what characteristics you want to change.") #if user decided to change the stats pf the card then program asks what characteristics user wants to change
                        if change_characteristic is None:
                            easygui.msgbox("Cancelled.") #if user presses the "cancel" button the loops breaks and it goes to the main menu
                            menu()
                            break
                        elif not change_characteristic:
                            easygui.msgbox("Enter the characteristic.") #if user didnt entered anything or just pressed enter then loop is restarts
                            continue
                        
                        elif change_characteristic.title() not in cards[change_characteristic_id.title()]: 
                                    easygui.msgbox("No such characteristic!") #if there is no such characteristic in the dictionary
                                    continue
                        
                        elif change_characteristic.title() in cards[change_characteristic_id.title()]: 
                            while True:
                                new_characteristic = easygui.integerbox("Please enter new characteristic stat") #if the programm finds the characteridtic it asks for the new value
                                if new_characteristic < 1:
                                    easygui.msgbox("Too short. Minimum data is - 1.") #if user entered something under 1
                                    continue
                                elif new_characteristic > 25:
                                    easygui.msgbox("Too much. Maximum is 25.") #if user entered something more than 25
                                    continue
                                else:
                                    cards[change_characteristic_id.title()][change_characteristic.title()] = new_characteristic #change the old characteristic to the new one
                                    easygui.msgbox("The card has been changed.")
                                    menu()
                                    break


def add():
    while True:
        namecard = easygui.enterbox("Please write the NAME of your card")
        if namecard is None:
            easygui.msgbox("Cancelled.")
            del cards[namecard]
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
        else:
            cards[namecard.title()] = {}
            break
             
    while True:
        strength = easygui.integerbox("Please write STRENGTH of your card")
        if strength is None:
            easygui.msgbox("Cancelled.")
            del cards[namecard.title()]
            menu()
            break
        elif not strength:
            easygui.msgbox("Enter the strength.")
            continue
        elif strength < 1:
            easygui.msgbox('Minimum characters in strength is 1')
            continue
        elif strength > 25:
            easygui.msgbox('Maximum characters in strength is 25')
            continue
        else:
            cards[namecard.title()]["Strength"] = strength
            break

    while True:
        speed = easygui.integerbox("Please write SPEED of your card")
        if speed is None:
            easygui.msgbox("Cancelled.")
            del cards[namecard.title()]
            menu()
            break
        elif not speed:
            easygui.msgbox("Enter the speed.")
            continue
        elif speed < 1:
            easygui.msgbox('Minimum characters in speed is 1')
            continue
        elif speed > 25:
            easygui.msgbox('Maximum characters in speed is 25')
            continue
        else:
            cards[namecard.title()]["Speed"] = speed
            break
        
    while True:
        stealth = easygui.integerbox("Please write STEALTH of your card")
        if stealth is None:
            easygui.msgbox("Cancelled.")
            del cards[namecard.title()]
            menu()
            break
        elif not stealth:
            easygui.msgbox("Enter the stealth.")
            continue
        elif stealth < 1:
            easygui.msgbox('Minimum characters in stealth is 1')
            continue
        elif stealth > 25:
            easygui.msgbox('Maximum characters in stealth is 25')
            continue
        else:
            cards[namecard.title()]["stealth"] = stealth
            break
    
    while True:
        cunning = easygui.integerbox("Please write CUNNING of your card")
        if cunning is None:
            easygui.msgbox("Cancelled.")
            del cards[namecard.title()]
            menu()
            break
        elif not cunning:
            easygui.msgbox("Enter the cunning.")
            continue
        elif cunning < 1:
            easygui.msgbox('Minimum characters in cunning is 1')
            continue
        elif cunning > 25:
            easygui.msgbox('Maximum characters in cunning is 25')
            continue
        else:
            cards[namecard.title()]["cunning"] = cunning
            easygui.msgbox("Card successfully added!")
            menu()
            break      
        


def exit():
     sys.exit()


starting = easygui.buttonbox("Welcome!", "welcome", choices = ["Start"])
if not starting:
     exit()
else:
     menu()
