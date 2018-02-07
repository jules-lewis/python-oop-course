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

sword = Item("Sword")
sword.description = "Glamdring: white and gold, in an ivory sheath."
sword.describe()

lamp = Item("Lamp")
lamp.description = "The textile shade provides a diffused and decorative light."
lamp.describe()

current_room = kitchen
while True:		
    current_room.describe()         
    command = input("> ")    
    current_room = current_room.move(command)
    print()










