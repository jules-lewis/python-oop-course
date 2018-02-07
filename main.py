from room import Room
from item import Item
from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"

kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"

dining_hall = Room("Dining Hall")
dining_hall.description = "A large room with ornate golden decorations on each wall."
dining_hall.character = dave

ballroom = Room("Ballroom")
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

current_room = kitchen
current_room.describe()  
game_loop = True

while game_loop:		
    command = input("> ")
    if command == "help":
        print("Available commands are: north, east, south, west, talk, fight, help, quit.")
    elif command in ["north", "east", "south", "west"]:
        current_room = current_room.move(command)
        current_room.describe()
    elif command == "quit":
        game_loop = False
    elif command == "talk":
        if current_room.character == None:
            print("There is no one to talk to!")
        else:
            current_room.character.talk()
    elif command == "fight":
        if current_room.character == None:
            print("There is no one to fight!")
        else:
            print("What will you fight with?")
            fight_with = input()
            game_loop = current_room.character.fight(fight_with)
            if not game_loop:
                print("GAME OVER")
    else:
        print("I didn't recognise that command. Hint: try 'help'.")
    print()
