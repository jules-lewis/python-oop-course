from character import Character, Enemy

dave = Character("Dave", "A smelly zombie")
dave.set_conversation("Paris in the the Spring")
dave.describe()
dave.talk()

fred = Enemy("Fred", "Like a zombie, but worse.")
fred.set_conversation("Prepare to die!")
fred.describe()
fred.talk()
fred.weakness = "Silver bullet"

print("What will you fight with?")
fight_with = input()
fred.fight(fight_with)

