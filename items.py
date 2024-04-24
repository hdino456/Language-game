class Item:
    def __init__(self, item_name):
        self.name = item_name
        
    def set_descsription(self, item_description):
        self.description = item_description
    
    def get_description(self):
        print(f"{self.name}, {self.description}")
        
    pass