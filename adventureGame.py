import sys

from utils import split_string_length
from utils import cutscene
from utils import generate_item_sentence

import json
from rich.console import Console

console = Console()

console.print("Hello", style="green")


console.print("    ███████╗░█████╗░██████╗░██╗░░██╗  ██╗", style="BOLD")
console.print("    ╚════██║██╔══██╗██╔══██╗██║░██╔╝  ██║", style="BOLD")
console.print("    ░░███╔═╝██║░░██║██████╔╝█████═╝░  ██║", style="BOLD")
console.print("    ██╔══╝░░██║░░██║██╔══██╗██╔═██╗░  ██║", style="BOLD")
console.print("    ███████╗╚█████╔╝██║░░██║██║░╚██╗  ██║", style="BOLD")
console.print("    ╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝", style="BOLD")


console.print("░█▀▀█ █▀▀ █▀▄▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀ █▀▀▄")
console.print("░█▄▄▀ █▀▀ █─▀─█ █▄▄█ ▀▀█ ──█── █▀▀ █▄▄▀ █▀▀ █──█")
console.print("░█─░█ ▀▀▀ ▀───▀ ▀──▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀─")

class Item:
    def __init__(self, name, description, static, static_message):
        self.name = name
        self.description = description
        self.static = static
        self.static_message = static_message

    def interact(self):
        print(f"You interact with the {self.name}.")  # Customize this method for specific interactions.


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

    def get_times_entered(self):
        return self.times_entered


class Game:
    def __init__(self):
        self.current_room = None
        self.rooms = {}
        self.inventory = []

    # def load_rooms(self, filename):
    # with open(filename, 'r') as file:
    #     lines = file.readlines()
    #
    #     for line in lines:
    #         data = line.strip().split(':')
    #         room_name = data[0]
    #         room_desc = data[1]
    #         connections = data[2].split(',')
    #
    #         room = Room(room_name, room_desc)
    #         #print(f"Room: {room_name}, Desc: {room_desc}, Connections: {connections}")  # For debugging
    #
    #         if len(data) > 3:
    #             items = data[3].split('|')
    #             #print(items)
    #             #items = data[3:]
    #             for item in items:
    #                 item_data = item.split('=')
    #                 item_name = item_data[0]
    #                 item_desc = item_data[1]
    #                 static = False
    #                 if len(item_data) > 2 and "static" in item_data[2]:
    #                     static = True
    #                 room.add_item(Item(item_name, item_desc, static))
    #
    #         for connection in connections:
    #             conn_parts = connection.split('=')
    #             direction = conn_parts[0]
    #             connected_room = conn_parts[1]
    #             room.add_connection(direction, connected_room)
    #
    #         self.rooms[room_name] = room

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
                print(f"Room: {room_name}, Desc: {room_desc}, Connections: {connections}")  # For debugging

                if 'items' in room_data:
                    items = room_data['items']
                    for item_data in items:
                        item_name = item_data['name']
                        item_desc = item_data['description']
                        static = item_data.get('static', False)
                        static_message = item_data.get('static_message', None)

                        room.add_item(Item(item_name, item_desc, static, static_message))

                for direction, connected_room in connections.items():
                    room.add_connection(direction, connected_room)

                self.rooms[room_name] = room

    def start_game(self, start_room):
        self.current_room = self.rooms[start_room]

        if self.current_room.times_entered == 0:
            cutscene(self.current_room.enter_cutscene, 400)
        self.current_room.times_entered += 1

        print(split_string_length(self.current_room.description, 400))

        items = self.current_room.get_items()
        item_Names = []

        if items:
            for item in items:
                item_Names.append(item.name)

            print(generate_item_sentence(item_Names))
        else:
            print("There are no items in the room.")

        self.prompt()

    def prompt(self):
        while True:
            command = input("Enter a command: (TYPE --help FOR MORE COMMANDS)").lower()

            if command == "quit":
                print("Game over. Goodbye!")
                return

            if command == "n".casefold() or "north".casefold() in command or command == "s".casefold() or "south".casefold() in command or command == "e".casefold() or "east".casefold() in command or command == "w".casefold() or "west".casefold() in command:
                if command == "n".casefold() or "north".casefold() in command:
                    self.move("north")
                if command == "s".casefold() or "south".casefold() in command:
                    self.move("south")
                if command == "e".casefold() or "east".casefold() in command:
                    self.move("east")
                if command == "w".casefold() or "west".casefold() in command:
                    self.move("west")
            elif command.startswith("look at ".casefold()):
                self.look(command[8:])

            elif command.startswith("take "):
                item_name = command[5:]
                self.take_item(item_name)
            elif command.startswith("drop "):
                item_name = command[5:]
                self.drop_item(item_name)
            elif command.startswith("interact with "):
                item_name = command[14:]
                self.interact_with_item(item_name)
            elif "inventory".casefold() in command or command == "i".casefold() or command == "inv".casefold():
                self.display_inventory()
            elif command == "exit".casefold() or command == "leave".casefold():
                leave_ = input("Are you sure you want to leave the game?")
                if leave_ == "yes".casefold():
                    sys.exit()
                elif leave_ == "no".casefold():
                    print("Sure thing! ")
                    self.prompt()
                else:
                    print("Invalid command!")
            else:
                print("Invalid command!")

    def move(self, direction):
        next_room = self.current_room.get_connection(direction)

        if next_room:
            self.current_room = self.rooms[next_room]

            if self.current_room.times_entered == 0:
                cutscene(self.current_room.enter_cutscene, 400)
            self.current_room.times_entered += 1

            print(split_string_length(self.current_room.description, 400))
            items = self.current_room.get_items()
            item_Names = []
            if items:
                for item in items:
                    item_Names.append(item.name)
                print(generate_item_sentence(item_Names))
            else:
                print("There are no items in the room.")
        else:
            print("You can't go that way!")

        self.prompt()

    def look(self, input_item):
        items = self.current_room.get_items()

        # print(f"{self.current_room.description}")
        if items:
            for item in items:
                if input_item == item.name:
                    print(item.description)

        else:
            print("There are no items in the room.")

    def take_item(self, item_name):
        items = self.current_room.get_items()

        for item in items:
            if item.name == item_name:
                if item.static:
                    static_message = item.static_message
                    if static_message:
                        print(static_message)
                    else:
                        print("That item is too heavy to pick up.")

                else:
                    self.current_room.remove_item(item)
                    self.inventory.append(item)
                    print(f"You take the {item_name}.")
                return

        print("That item is not in the room.")

    def drop_item(self, item_name):
        items = []

        if self.inventory:
            for item in self.inventory:
                items.append(item)
        else:
            print("Your inventory is empty.")
            return

        for item in items:
            if item.name == item_name:
                if item.static:
                    print("That item can't be dropped")
                else:
                    self.current_room.add_item(item)
                    self.inventory.remove(item)
                    print(f"You drop the {item_name}.")
                return

        print("That item is not in the room.")

    def interact_with_item(self, item_name):
        items = self.current_room.get_items()

        for item in items:
            if item.name == item_name:
                item.interact()
                return

        print("That item is not in the room.")

    def display_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")


if __name__ == "__main__":
    game = Game()
    game.load_rooms("rooms.json")
    game.start_game("YourBedroom")
