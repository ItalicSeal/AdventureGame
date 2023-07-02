import sys

from rich.console import Console

from adventureGame import Game
console = Console()

def main_menu():
    response = input("> ")
    if response.lower() == "play":
        game = Game()
        game.load_rooms("rooms.json")
        game.start_game("YourBedroom")
    elif response.lower() == "options":
        console.print("█▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▄░█ █▀")
        console.print("█▄█ █▀▀ ░█░ █ █▄█ █░▀█ █░▀█ ▄█")
        console.print("---DIFFICULTY---")
        console.print("-EASY")
        console.print("-Medium")
        console.print("-HARD")
        console.print("-VETERAN")
        console.print("")
        console.print("---Back---")
        response = input("> ")
        console.print("    ███████╗░█████╗░██████╗░██╗░░██╗  ██╗")
        console.print("    ╚════██║██╔══██╗██╔══██╗██║░██╔╝  ██║")
        console.print("    ░░███╔═╝██║░░██║██████╔╝█████═╝░  ██║")
        console.print("    ██╔══╝░░██║░░██║██╔══██╗██╔═██╗░  ██║")
        console.print("    ███████╗╚█████╔╝██║░░██║██║░╚██╗  ██║")
        console.print("    ╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝")
        console.print("░█▀▀█ █▀▀ █▀▄▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀ █▀▀▄")
        console.print("░█▄▄▀ █▀▀ █─▀─█ █▄▄█ ▀▀█ ──█── █▀▀ █▄▄▀ █▀▀ █──█")
        console.print("░█─░█ ▀▀▀ ▀───▀ ▀──▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀─")
        console.print("---PLAY---")
        console.print("---OPTIONS---")
        console.print("---Quit---")
        main_menu()
    elif response.lower() == "exit" or response.lower() == "leave" or response.lower() == "quit":
        console.print("Goodbye!")
        sys.exit()
    else:
        print("Invalid Command!")
        main_menu()

console.print("    ███████╗░█████╗░██████╗░██╗░░██╗  ██╗")
console.print("    ╚════██║██╔══██╗██╔══██╗██║░██╔╝  ██║")
console.print("    ░░███╔═╝██║░░██║██████╔╝█████═╝░  ██║")
console.print("    ██╔══╝░░██║░░██║██╔══██╗██╔═██╗░  ██║")
console.print("    ███████╗╚█████╔╝██║░░██║██║░╚██╗  ██║")
console.print("    ╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝")
console.print("░█▀▀█ █▀▀ █▀▄▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀ █▀▀▄")
console.print("░█▄▄▀ █▀▀ █─▀─█ █▄▄█ ▀▀█ ──█── █▀▀ █▄▄▀ █▀▀ █──█")
console.print("░█─░█ ▀▀▀ ▀───▀ ▀──▀ ▀▀▀ ──▀── ▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀─")
console.print("---PLAY---")
console.print("---OPTIONS---")
console.print("---Quit---")

main_menu()
