from room import Room
from items import Item

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dhl = Room("Dining Hall")

colt45 = Item("Colt 45")

kitchen.set_description("A dank and drity room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor; chandallere hanging from the wall")
dhl.set_description("A room with a long mahagony table with huge candlesticks in the middle of it.")

colt45.set_descsription("an old gun with a brown wooden handle and datk stanes on the glossy metal.")

kitchen.link_room(dhl,"South")
dhl.link_room(kitchen,"North")
dhl.link_room(ballroom,"West")
ballroom.link_room(dhl,"East")

current_room = kitchen


while True:
    print("\n")
    current_room.get_description()
    command = input("Which way do you want to go? ")
    current_room = current_room.move(command)
    if current_room is dhl:
        print(f"On the dining table you can find {colt45.get_description()}")
    else:
        pass 

