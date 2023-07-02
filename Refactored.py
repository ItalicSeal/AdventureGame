import json
from utils import split_string_length
from utils import cutscene

split_length = 400


class Item:
    def __init__(self, name, description, take):
        self.name = name
        self.description = description
        self.take = take


class Room:
    def __init__(self, name, description, north_cell, east_cell, south_cell, west_cell, objects):
        self.name = name
        self.description = description
        self.north_cell = north_cell
        self.east_cell = east_cell
        self.south_cell = south_cell
        self.west_cell = west_cell
        self.objects = objects

    @classmethod
    def room_entered(cls, room):
        print(split_string_length(room.description, split_length))

        if room.objects:
            object_list = ', a '.join(room.objects)
            print(f"You can see a {object_list}.\n")

        room.get_input()

    def get_input(self):
        while True:
            player_input = input("What do you do next? (You can use --help for more info) ")

            if player_input == "--help":
                print("1. Head north\n2. Head east\n3. Head south\n4. Head west\n5. Description/resay\n6. Inventory/i\n")
            #elif player_input.casefold() in ['inventory', 'i', 'inv']:
            #    print(f"Inventory: \n{inventory}")
            elif player_input.casefold() in ['north', 'n']:
                self.head_direction('north')
            elif player_input.casefold() in ['east', 'e']:
                self.head_direction('east')
            elif player_input.casefold() in ['south', 's']:
                self.head_direction('south')
            elif player_input.casefold() in ['west', 'w']:
                self.head_direction('west')
            else:
                print("I don't understand your command.")

    def head_direction(self, direction):
        next_room = getattr(self, f'{direction}_cell')

        if next_room.casefold() == '':
            print(f"\nThere is nothing that way.\n")
        elif 'message' in next_room:
            print(f"\n{next_room.replace('message: ', '')}\n")
        else:
            print(f'\nYou head {direction}\n')
            Room.room_entered(eval(next_room))


def main():
    cutscene([
        "You wake up with a start as a deafening thunderclap shakes the house. Your heart is racing but you lie frozen "
        "in bed, confused and disoriented. Where are you? What's going on? All you hear is the steady patter of gushing "
        "rain against the roof above and the ragged wind rattling the windowpanes. After a few moments of blinking "
        "into the darkness, you start to remember. You're at home, in your own room, in your own bed. You were having "
        "some sort of nightmare, but you can't quite remember what it was.",
        "You realize that your bladder is bursting. You really need to pee! Unfortunately, the toilet is down the hall..."
    ], split_length)

    inventory = []

    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)["cell"]
        players_room = Room(
            data[0]["name"], data[0]["description"],
            data[0]["northCell"], data[0]["eastCell"],
            data[0]["southCell"], data[0]["westCell"],
            data[0]["objects"]
        )
        hallway = Room