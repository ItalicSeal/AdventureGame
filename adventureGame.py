import sys
from utils import split_string_length
from utils import cutscene
from utils import generate_item_sentence

import logging

import json
from rich.console import Console

from utils import split_string_length

console = Console()

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Item:
    def __init__(self, name, description, static, static_message):
        self.name = name
        self.description = description
        self.static = static
        self.static_message = static_message
        self.modules = []

        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You put the {item.name} into the {self.name}.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"You took the {item.name} from the {self.name}.")
        else:
            print(f"The {item.name} is not in the {self.name}.")

    def add_modules(self, modules):
        self.modules.extend(modules)

    def has_module(self, module):
        return module in self.modules


class Container(Item):
    def __init__(self, name, description, static, static_message):
        super().__init__(name, description, static, static_message)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def has_item(self, item):
        return item in self.items


class Room:
    def __init__(self, name, description, enter_cutscene):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []
        self.times_entered = 0
        self.enter_cutscene = enter_cutscene

    def add_connection(self, direction, room):
        self.connections[direction] = room

    def get_connection(self, direction):
        return self.connections.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def get_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                return item

        return None

    def get_times_entered(self):
        return self.times_entered


class Game:
    def __init__(self):
        self.current_room = None
        self.rooms = {}
        self.inventory = []

    def load_rooms(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

            for room_data in data:
                room_name = room_data['name']
                room_desc = room_data['description']
                connections = room_data['connections']
                if 'enter_cutscene' in room_data:
                    enter_cutscene = room_data.get('enter_cutscene', None)

                room = Room(room_name, room_desc, enter_cutscene)
                # console.print(f"Room: {room_name}, Desc: {room_desc}, Connections: {connections}")  # For debugging

                if 'items' in room_data:
                    items = room_data['items']
                    for item_data in items:
                        item_name = item_data['name']
                        item_desc = item_data['description']
                        static = item_data.get('static', False)
                        static_message = item_data.get('static_message', None)

                        item_modules = item_data.get('modules', [])

                        item = Item(item_name, item_desc, static, static_message)

                        item.add_modules(item_modules)

                        room.add_item(item)

                for direction, connected_room in connections.items():
                    room.add_connection(direction, connected_room)

                self.rooms[room_name] = room

    def start_game(self, start_room):
        
        self.current_room = self.rooms[start_room]
        console.print(self.current_room.name, style="green underline bold")

        if self.current_room.times_entered == 0:
            cutscene(self.current_room.enter_cutscene, 400)
        self.current_room.times_entered += 1

        console.print(split_string_length(self.current_room.description, 400))

        items = self.current_room.get_items()
        item_names = []

        if items:
            for item in items:
                item_names.append(item.name)

            console.print(generate_item_sentence(item_names))
        else:
            console.print("There are no items in the room.")

        self.prompt()

    def prompt(self):
        while True:
            command = input("> ").lower()
            verbs = ["take", "drop", "put", "open", "close", "go", "travel", "head", "move", "north", "south", "east",
                     "west", "leave", "quit", "exit", "n", "s", "e", "w"]
            # nouns =

            for i in verbs:
                if command.startswith(i):
                    logging.debug("Valid verb")
                    break
            for i in ["take", "drop", "put", "open", "close"]:
                if command.startswith(i):
                    self.interact_with_item(command)
                    break
            for i in ["go", "travel", "head", "move"]:
                if command.startswith(i):
                    logging.debug("Movement")
                    self.move(command)
                    break
            for i in ["north", "south", "east", "west", "n", "s", "e", "w"]:
                if command == i:
                    logging.debug("Movement")
                    self.move(command)
                    break
            for i in ["leave", "quit", "exit"]:
                if command.startswith(i):
                    leave_ = input("Are you sure you want to leave the game?")
                    if leave_ == "yes".casefold() or leave_ == "y".casefold():
                        sys.exit()
                    elif leave_ == "no".casefold() or leave_ == "n".casefold():
                        console.print("Sure thing! ")
                        self.prompt()
                        break
                    else:
                        console.print("Invalid command!")
                        break
            console.print("[red]Invalid Command![/]")

            # if command == "n".casefold() or "north".casefold() in command or command == "s".casefold() or "south".casefold() in command or command == "e".casefold() or "east".casefold() in command or command == "w".casefold() or "west".casefold() in command:
            #     if command == "n".casefold() or "north".casefold() in command:
            #         self.move("north")
            #     if command == "s".casefold() or "south".casefold() in command:
            #         self.move("south")
            #     if command == "e".casefold() or "east".casefold() in command:
            #         self.move("east")
            #     if command == "w".casefold() or "west".casefold() in command:
            #         self.move("west")
            # elif command.startswith("look at ".casefold()):
            #     self.look(command[8:])
            # elif command.startswith("take "):
            #     item_name = command[5:]
            #     self.take_item(item_name)
            # elif command.startswith("drop "):
            #     item_name = command[5:]
            #     self.drop_item(item_name)
            # elif command.startswith("interact with "):
            #     item_name = command[14:]
            #     self.interact_with_item(item_name, "put")
            # elif "inventory".casefold() in command or command == "i".casefold() or command == "inv".casefold():
            #     self.display_inventory()

    #
    # elif command.lower() == "exit" or command.lower() == "leave" or command.lower() == "quit":
    #     leave_ = input("Are you sure you want to leave the game?")
    #     if leave_ == "yes".casefold() or leave_ == "y".casefold():
    #         sys.exit()
    #     elif leave_ == "no".casefold() or leave_ == "n".casefold():
    #         console.print("Sure thing! ")
    #         self.prompt()
    #     else:
    #         console.print("Invalid command!")
    # else:
    #     console.print("Invalid command!")

    def move(self, command):
        direction = ""
        for i in command.split():
            if i == "north" or i == "n":
                direction = "north"
            elif i == "east" or i == "e":
                direction = "east"
            elif i == "south" or i == "s":
                direction = "south"
            elif i == "west" or i == "w":
                direction = "west"

        next_room = self.current_room.get_connection(direction)

        if next_room:
            self.current_room = self.rooms[next_room]

            console.print(self.current_room.name, style="green underline bold")

            if self.current_room.times_entered == 0:
                cutscene(self.current_room.enter_cutscene, 400)
            self.current_room.times_entered += 1

            console.print(split_string_length(self.current_room.description, 400))
            items = self.current_room.get_items()
            item_names = []
            if items:
                for item in items:
                    item_names.append(item.name)
                console.print(generate_item_sentence(item_names))
            else:
                console.print("There are no items in the room.")
        else:
            console.print("You can't go that way!")

        self.prompt()

    def look(self, input_item):
        items = self.current_room.get_items()

        # console.print(f"{self.current_room.description}")
        if items:
            for item in items:
                if input_item == item.name:
                    console.print(item.description)

        else:
            console.print("There are no items in the room.")

    def take_item(self, item_name):
        items = self.current_room.get_items()

        for item in items:
            if item.name == item_name:
                if item.static:
                    static_message = item.static_message
                    if static_message:
                        console.print(static_message)
                    else:
                        console.print("That item is too heavy to pick up.")

                else:
                    self.current_room.remove_item(item)
                    self.inventory.append(item)
                    console.print(f"You take the [green bold]{item_name}.[/]")
                return

        console.print("That item is not in the room.")

    def drop_item(self, item_name):
        items = []

        if self.inventory:
            for item in self.inventory:
                items.append(item)
        else:
            console.print("Your inventory is empty.")
            return

        for item in items:
            if item.name == item_name:
                if item.static:
                    console.print("That item can't be dropped")
                else:
                    self.current_room.add_item(item)
                    self.inventory.remove(item)
                    console.print(f"You drop the [green bold]{item_name}[/].")
                return

        console.print("That item is not in the room.")

    def interact_with_item(self, message):

        if message.startswith("put"):
            item = message[4:].split(" in ")[0].replace(" ", "")
            container = message[4:].split(" in ")[1].replace(" ", "")
            self.put_in_container(item, container)

        # if item:
        #    if item.has_module("container"):
        #        if interaction == "take":
        #            self.take_from_container(item)
        #        elif interaction == "put":
        #            self.put_in_container(item)
        #        else:
        #            print(f"You can't {interaction} the {item_name}.")
        #    else:
        #        print(f"The {item_name} cannot be interacted with.")
        # else:
        #    print("That item is not in the room.")

    def display_inventory(self):
        if self.inventory:
            console.print("Inventory:")
            for item in self.inventory:
                console.print(f"- [green bold]{item.name}[/]: [cyan]{item.description}[/]")
        else:
            console.print("Your inventory is empty.")

    def take_from_container(self, container):
        # Perform the logic for taking items from the container
        print(f"You take something from the {container.name}.")

    def put_in_container(self, item_name, container_name):
        # Perform the logic for putting items into the container
        item = self.get_item_from_inventory(item_name)
        container = self.get_item_from_inventory(container_name)
        if container is None:
            container = self.current_room.get_item(container_name)

        if item:
            if container:
                if container.has_module("container"):
                    console.print(f"You put the [green]{ptingitem.name}[/] into the [green]{plcing.name}[/].")
            else:
                console.print(f"Container, {container_name} not found. ")
        else:
            console.print(f"Item, {item_name} not found. ")

        # for ptingitem in inventory_items:
        #    if ptingitem.name == item:
        #        for plcing in items:
        #            if plcing.name == container:
        #                if plcing.has_module("container"):
        #                    console.print(f"You put the [green]{ptingitem.name}[/] into the [green]{plcing.name}[/].")
        #                    break
        #                else:
        #                    console.print(f"The [green]{plcing.name}[/] is not a container")
        #                    break

    def get_item_from_inventory(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        return None

# if __name__ == "__main__":
#    game = Game()
#    game.load_rooms("rooms.json")
#    game.start_game("YourBedroom")
