import json
from utils import split_string_length

split_length = 400

class Cell(object):
    timesEntered = 0

    def __init__(self, name, firstTimeDescription, description, northCell, eastCell, southCell, westCell, objects):
        self.name = name
        self.firstTimeDescription = firstTimeDescription
        self.description = description

        self.northCell = northCell
        self.eastCell = eastCell
        self.southCell = southCell
        self.westCell = westCell

        self.objects = objects

    @staticmethod
    def getInput(cls):
        playerInput = input("What do you do next?(You can use --help for more info) ")
        if playerInput == "--help":
            print(
                "1. Head north \n2. Head east \n3. Head south \n4. Head west \n5. Description/resay \n6. Inventory/i \n")
            cls.getInput(cls)
        elif 'inventory' in playerInput.casefold() or playerInput.casefold() == "i" or playerInput.casefold() == "inv":
            print("Inventory: \n" + str(inventory))
        elif 'north' in playerInput.casefold() or playerInput.casefold() == "n":
            cls.headNorth(cls)
        elif 'east' in playerInput.casefold() or playerInput.casefold() == "e":
            cls.headEast(cls)
        elif 'south' in playerInput.casefold() or playerInput.casefold() == "s":
            cls.headSouth(cls)
        elif 'west' in playerInput.casefold() or playerInput.casefold() == "w":
            cls.headWest(cls)
        elif 'description' in playerInput.casefold() or 'resay' in playerInput.casefold():
            cls.timesEntered = 0
            cls.room_entered(cls)
        else:
            print("\n" + firstName + "I don't understand your command")
            cls.room_entered(cls)

    @staticmethod
    def headNorth(cls):
        if cls.northCell == "".casefold():
            print("\nThere is nothing that way.\n")
            cls.getInput(cls)
        elif 'message' in cls.northCell:
            print("\n" + cls.northCell.replace('message: ', '') + "\n")
            cls.getInput(cls)
        else:
            print('\nYou head north\n')
            Cell.room_entered(eval(cls.northCell))

    @staticmethod
    def headEast(cls):
        if cls.eastCell == "".casefold():
            print("\nThere is nothing that way.\n")
            cls.getInput(cls)
        elif 'message' in cls.eastCell:
            print("\n" + cls.eastCell.replace('message: ', '') + "\n")
            cls.getInput(cls)
        else:
            print('\nYou head east\n')
            Cell.room_entered(eval(cls.eastCell))

    @staticmethod
    def headSouth(cls):
        if cls.southCell == "".casefold():
            print("\nThere is nothing that way.\n")
            cls.getInput(cls)
        elif 'message' in cls.southCell:
            print("\n" + cls.southCell.replace('message: ', '') + "\n")
            cls.getInput(cls)
        else:
            print('\nYou head south\n')
            Cell.room_entered(eval(cls.southCell))

    @staticmethod
    def headWest(cls):
        if cls.westCell == "".casefold():
            print("\nThere is nothing that way.\n")
            cls.getInput(cls)
        elif 'message' in cls.westCell:
            print("\n" + cls.westCell.replace('message: ', '') + "\n")
            cls.getInput(cls)
        else:
            print('\nYou head west\n')
            Cell.room_entered(eval(cls.westCell))

    @staticmethod
    def room_entered(cls):
        print("\nYou are in " + cls.name + ": \n")

        cls.timesEntered += 1
        if cls.timesEntered == 1:
            print(split_string_length(cls.firstTimeDescription, split_length))
            #
        else:
            print(cls.description + "\n")
        cls.getInput(cls)


# Start of adventure
#print("Hello fellow adventurer!")
#firstName = input("What is your first name? ").replace(" ", "")
#lastName = input("What is your last name? ").replace(" ", "")

inventory = []

print("\nWelcome " + firstName + " " + lastName + " to the wonderful world of Elysiuma")

with open("rooms.json", "r") as json_file:
    data = (json.load(json_file)["cell"])
    number = 0

    # for i in (data[number]["name"]):
    #    print(data)
    #     number += 1

    The_Shadows_Den_Bar = Cell(data[1]["name"], data[1]["firstTimeDescription"], data[1]["description"],
                               data[1]["northCell"], data[1]["eastCell"],
                               data[1]["southCell"], data[1]["westCell"], ['screwdriver'])
    The_Shadow_Den = Cell(data[0]["name"], data[0]["firstTimeDescription"], data[0]["description"],
                          data[0]["northCell"], data[0]["eastCell"],
                          data[0]["southCell"], data[0]["westCell"], ['screwdriver'])

Cell.room_entered(The_Shadow_Den)
