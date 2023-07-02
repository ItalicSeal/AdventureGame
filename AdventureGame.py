import json
from utils import split_string_length
from utils import cutscene

split_length = 400


class Item(object):
    def __init__(self, name, description, take):
        self.name = name
        self.description = description
        self.take = take


    def get_name(cls):
        return cls.name

    # @staticmethod
    # def get_description(cls):


class Cell(object):
    timesEntered = 0

    def __init__(self, name, description, northCell, eastCell, southCell, westCell, objects):
        self.name = name
        self.description = description

        self.northCell = northCell
        self.eastCell = eastCell
        self.southCell = southCell
        self.westCell = westCell

        self.objects = objects

    @staticmethod
    def getInput(cls):
        playerInput = input("What do you do next?(You can use --help for more info) ")

        for object in cls.objects:
            #if object in playerInput:
                #interacted
            #if object in playerInput:
            #    interactedObject = eval(object)
            #    name = object.get_name
            #    print(name)

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
            # print("\n" + firstName + "I don't understand your command")
            print("I don't understand your command.")

            cls.getInput(cls)

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
        print(split_string_length(cls.description, split_length))

        # objects = []
        length = len(cls.objects)
        string = ""
        if length != 0:
            if length == 1:
                string += cls.objects[0]
            else:
                currentlength = 0
                for object in cls.objects:
                    currentlength += 1
                    if currentlength >= length:
                        string += " and a " + object
                    elif currentlength >= length - 1:
                        string += object
                    else:
                        string += object + ", a "
        print("You can see a " + str(string) + ". \n")


        length = len(cls.objects)
        string = ""

        if length == 1:
            string = cls.objects[0]
        elif length > 1:
            string = ", ".join(cls.objects[:-1]) + " and " + cls.objects[-1]

        if string:
            print(f"You can see {string}.")
        else:
            print("There are no objects to see.")

        cls.getInput(cls)


# Start of adventure
# print("Hello fellow adventurer!")
# firstName = input("What is your first name? ").replace(" ", "")
# lastName = input("What is your last name? ").replace(" ", "")

cutscene([
             "You wake up with a start as a deafening thunderclap shakes the house. Your heart is racing but you lie frozen in bed, confused and disoriented. Where are you? What's going on? All you hear is the steady patter of gushing rain against the roof above and the ragged wind rattling the windowpanes. After a few moments of blinking into the darkness, you start to remember. You're at home, in your own room, in your own bed. You were having some sort of nightmare, but you can't quite remember what it was. ",
             "You realize that your bladder is bursting. You really need to pee! Unfortunately, the toilet is down the hall... "],
         split_length)

inventory = []

# print("\nWelcome " + firstName + " " + lastName + " to the wonderful world of Elysiuma")

with open("rooms.json", "r") as json_file:
    data = (json.load(json_file)["cell"])
    number = 0

    Players_Room = Cell(data[0]["name"], data[0]["description"],
                        data[0]["northCell"], data[0]["eastCell"],
                        data[0]["southCell"], data[0]["westCell"], data[0]["objects"])
    Hallway = Cell(data[1]["name"], data[1]["description"],
                   data[1]["northCell"], data[1]["eastCell"],
                   data[1]["southCell"], data[1]["westCell"], data[1]["objects"])

with open("items.json", "r") as json_file:
    data = (json.load(json_file)["item"])

    bed = Item(data[0]["name"], data[0]["description"], data[0]["interactions"])

Cell.room_entered(Players_Room)
