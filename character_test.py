from character import Character, Enemy

dave = Character("Dave", "Smelly zombie")

greg = Enemy("Greg", "Daft cunt")

dave.set_conversation("gaaah, braaains...")

print("\n")

print(f"You have encauntered {greg.name} a {greg.description}")
greg.set_conversation("Oi! What ya sayin fam, wanna get foucking shanked?")

greg.talk()

greg.set_weakness("Bitch slap")

print("Fight Greg with:")
greg.fight(input())