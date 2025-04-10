import easygui #importing easyGUI

#nested dictionary of all cards
cards = {"STO":
            {"Name": "Stoneling", 
            "Strength": 7, 
            "Speed": 1, 
            "Stealth": 25, 
            "Cunning": 15},
        "VEX":
            {"Name": "Vexscream",
            "Strength": 1,
            "Speed": 6,
            "Stealth": 21,
            "Cunning": 19},
        "DAW":
            {"Name": "Dawnmirage",
            "Strength": 5,
            "Speed": 15,
            "Stealth": 18,
            "Cunning": 22},
        "BLA":
            {"Name": "Blazegolem",
            "Strength": 15,
            "Speed": 20,
            "Stealth": 23,
            "Cunning": 6},
        "WEB":
            {"Name": "Websnake",
            "Strength": 7,
            "Speed": 15,
            "Stealth": 10,
            "Cunning": 5},
        "MOL":
            {"Name": "Moldvine",
            "Strength": 21,
            "Speed": 18,
            "Stealth": 14,
            "Cunning": 5},
        "VOR":
            {"Name": "Vortexwing",
            "Strength": 19,
            "Speed": 13, 
            "Stealth": 19, 
            "Cunning": 2},
        "ROT":
            {"Name": "Rotthing", 
            "Strength": 16, 
            "Speed": 7, 
            "Stealth": 4, 
            "Cunning": 12},
        "FRO": 
            {"Name": "Froststep", 
            "Strength": 14, 
            "Speed": 14, 
            "Stealth": 17, 
            "Cunning": 4},
        "WIS": 
            {"Name": "Wispghoul",
            "Strength": 17, 
            "Speed": 19, 
            "Stealth": 3, 
            "Cunning": 2}}
while True: #all almost all of the code is on the loop so it can be returned to the menu
    menu = easygui.buttonbox("Select one of the options below.", "Options", choices = ["Cards", "Delete", "Add", "Change", "Search", "Exit"])
    #main menu with all buttons "cards" - show all cards "delete" - delete the card "add" - add the card "change" - change the card "exit" - exit the programm
    if menu == "Exit": #when user click "Exit" the loop is breaks
        break

    if menu == "Cards":
        message = ""
        for cards_id, cards_info in cards.items(): #go through all cards id and cards info in the dictionary
            message += f"Card ID: {cards_id}\n" #add the card id to the message
            for key, value in cards_info.items(): #go through all cards details in the cards_info 
                message += f" {key}: {value}\n" #add cards details (like speed, stealth)
        easygui.msgbox(message, "All cards") #displaying whole dictionary

    elif menu == "Delete":
        deleting = easygui.enterbox("Please write the ID of the card you want to delete.")
        del cards[deleting]


    elif menu == "Search": #searching information about the card by name
        display = ""
        display = "\n".join([f"{key}: {value}" for key, value in cards.items()])
        search = easygui.enterbox('Enter the name of the card for which you want to find information: ')
        for key,value in cards.items():
            display += "\n".join([f"{key}: {value}" for key, value in cards.items()])
            for k,v in value.items():
                if search==v:
                    display = "\n".join([f"{key}: {value}" for key, value in value.items()])
                    print(value.items())
                    easygui.msgbox(display)

    elif menu == "Change":
        while menu:
            change_characteristic_id = easygui.enterbox("Please write ID of card you want to change.")
            if change_characteristic_id not in cards:
                easygui.msgbox("There's no such ID!")
            else:
                break


        change_int_or_str = easygui.buttonbox("You want to change the name or stats?", "???", choices= ["Name", "stats"])

        if change_int_or_str == "Name":
            new_name = easygui.enterbox("Enter new name.")
            cards[change_characteristic_id]["Name"] = new_name
        
        elif change_int_or_str == "stats":
            while True:
                change_characteristic = easygui.enterbox("Please write what characteristics you want to change.")
                if change_characteristic not in cards[change_characteristic_id]:
                     easygui.msgbox("No such characteristic!")
                elif change_characteristic in cards[change_characteristic_id]:
                    new_characteristic = easygui.integerbox("Please enter new characteristic stat")
                    if new_characteristic < 1:
                        easygui.msgbox("Too short. Minimum data is - 1.")
                    elif new_characteristic > 25:
                        easygui.msgbox("Too much. Maximum is 25.")
                    else:
                        cards[change_characteristic_id][change_characteristic] = new_characteristic
                        break
        
    elif menu == "Add":
        ID = easygui.enterbox("Please write ID of your card")
        while ID:
                if len(ID) < 3:
                    easygui.msgbox("Too short! ID must consist of three letters (it is recommended to use the first three letters of the monster's name).")
                    ID = easygui.enterbox("Please write ID of your card")
                elif len(ID) > 3:
                    easygui.msgbox("Too long! ID must consist of three letters (it is recommended to use the first three letters of the monster's name).")
                    ID = easygui.enterbox("Please write ID of your card")    
                elif ID in cards:
                        easygui.msgbox('This ID alredy in the cards! Try another one')
                        ID = easygui.enterbox("Please write ID of your card")
                else:
                    cards[ID] = {}
                    break


        name = easygui.enterbox("Please write NAME of your card")            
        while name:
                
                if len(name) < 1:
                    easygui.msgbox('Minimum characters in name is 1')
                    name = easygui.enterbox("Please write NAME of your card")
                elif len(name) > 25:
                    easygui.msgbox('Maximum characters in name is 25')
                    name = easygui.enterbox("Please write NAME of your card")
                elif name in cards:
                    easygui.msgbox('This ID alredy in the cards! Try another one')
                    name = easygui.enterbox("Please write NAME of your card")
                else:
                    cards[ID]['Name'] = name
                break

        strength = easygui.integerbox("Please write STRENGTH of your card")
        while strength:
                if strength < 1:
                    easygui.msgbox('Minimum characters in strength is 1')
                    strength = easygui.integerbox("Please write STRENGTH of your card")
                elif strength > 25:
                    easygui.msgbox('Maximum characters in strength is 25')
                    strength = easygui.integerbox("Please write STRENGTH of your card")
                else:
                    cards[ID]["Strength"] = strength
                    break
        
        speed = easygui.integerbox("Please write SPEED of your card")
        while speed:
            if speed < 1:
                easygui.msgbox('Minimum characters in speed is 1')
                speed = easygui.integerbox("Please write SPEED of your card")
            elif speed > 25:
                easygui.msgbox('Maximum characters in speed is 25')
                speed = easygui.integerbox("Please write SPEED of your card")
            else:
                cards[ID]["Speed"] = speed
                break
        

        stealth = easygui.integerbox("Please write STEALTH of your card")
        while stealth:
            if stealth < 1:
                easygui.msgbox('Minimum characters in stealth is 1')
                stealth = easygui.integerbox("Please write STEALTH of your card")
            elif stealth > 25:
                easygui.msgbox('Maximum characters in stealth is 25')
                stealth = easygui.integerbox("Please write STEALTH of your card")
            else:
                cards[ID]["stealth"] = stealth
                break     

        cunning = easygui.integerbox("Please write CUNNING of your card")
        while cunning:
            if cunning < 1:
                easygui.msgbox('Minimum characters in cunnning is 1')
                cunning = easygui.integerbox("Please write CUNNING of your card")
            elif cunning > 25:
                easygui.msgbox('Maximum characters in cunning is 25')
                cunning = easygui.integerbox("Please write CUNNING of your card")
            else:
                cards[ID]["cunning"] = cunning
                break   


print(cards)