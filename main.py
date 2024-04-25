from room import Room
from items import Item
from character import Enemy

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

greg = Enemy("Greg", "Daft cunt")
greg.set_conversation("Oi! What ya sayin fam, wanna get foucking shanked?")
greg.set_weakness("Bitch slap")

dhl.set_character(greg)

current_room = kitchen

print("\n")
current_room.get_description()
while True:
    command = input("Which way do you want to go? ")
    if command in ["North", "South", "West", "East"]:
        current_room = current_room.move(command)
        current_room.get_description()
        inhabitant = current_room.get_character() 
        print(inhabitant)
         
        if current_room is dhl:
            print(f"On the dining table you can find {colt45.get_description()}")
            
    if inhabitant is not None:
        print(f"you have stummbled upon {inhabitant.name} a {inhabitant.description}")
        engage = input(f"Engage with {inhabitant.name}? Y/N ")
        if engage == "Y":
            inhabitant.talk()
            interaction = input("Talk, Fight or Walk away? " )
            if interaction == "Fight":   
                print("Fight with:")         
                fight = greg.fight(input())
                if fight is False:
                    print("Game over!")
                    break
            elif interaction == "Talk":
                inhabitant.talk()
            else:
                pass
    else:
        pass
