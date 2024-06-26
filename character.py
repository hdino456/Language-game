class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.response = None

    # Describe this character
    def describe(self):
        return self.description 

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
            
    def set_response(self,response):
        self.response = response
        
    def get_response(self):
        return self.response

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        
    def set_weakness(self,weakness):
        self.weakness = weakness
    
    def get_weakness(self):
        print(f"Enemyie's weakness is {self.weakness}")    
        pass
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You have defeated {self.name}")
            return True
        else:
            print(f"{self.name} has smashed you like a bug")
            return False