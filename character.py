from item import Item

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self._conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def conversation(self, character_conversation):
        self._conversation = character_conversation
    conversation = property(None, conversation)

    # Talk to this character
    def talk(self):
        if self._conversation is not None:
            print("[" + self.name + " says]: " + self._conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    _enemy_count = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy._enemy_count += 1
            
    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, enemy_weakness):
        self._weakness = enemy_weakness

    def enemy_count(self):
        return Enemy._enemy_count
    enemy_count = property(enemy_count, None)

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You defeat " + self.name + " with the " + combat_item +"!")
            Enemy._enemy_count -= 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.has_had_a_hug = False
        self.item_carried = None

    def set_item_carried(self, new_item):
        if new_item is not None:
            if isinstance(new_item, Item):
                self.item_carried = new_item
                return
        raise ValueError("new_item parameter should be of type Item.")
        
    def hug(self):
        if self.has_had_a_hug:
            print(self.name + " says 'One hug is fine thanks.'")
        else:
            print("You give " + self.name + " a lovely hug. " + self.name + " may be feeling generous now.")
            self.has_had_a_hug = True

    def ask(self):
        if self.item_carried is not None:
            if self.has_had_a_hug:
                return_item = Item(self.item_carried.name, self.item_carried.description)
                print(self.name + " gives you " + return_item.name + ".")
                self.item_carried = None
                return return_item
            else:
                print(self.name + " needs a hug.")
        else:
            print(self.name + " isn't carrying anything.")
