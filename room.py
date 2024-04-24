class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        
    def set_description(self, room_description):
        self.description = room_description
            
    def get_description(self):
        print(f"{self.name}, {self.description}") 
        
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        
    def print_dic(self):
        print(self.linked_rooms)
        
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\n")
            print("You can't go that way")
            return self
    pass