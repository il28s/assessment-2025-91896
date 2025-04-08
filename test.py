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

for cards_id, cards_info in cards.items():
    print("\nCard ID: ", cards_id)

    for key in cards_info:
        print(key + ":", cards_info[key])

