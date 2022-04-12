class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description  
        self.soft_spot = None
        self.affinity = 0
        self.conversation_0 = None
        self.conversation_1 = None  

    # Describe this character
    def describe(self):
        print(self.name + " (" + self.description +  ") is here.")

    #getter/setter for soft_spot
    def get_soft_spot(self):
        return self.soft_spot
    def set_soft_spot(self, soft_spot):
        self.soft_spot = soft_spot

    #getter/setter for affinity
    def get_affinity(self):
        return self.affinity
    def set_affinity(self, affinity):
        self.affinity = affinity

    def set_conversation_0(self, conversation):
        self.conversation_0 = conversation
    def set_conversation_1(self, conversation):
        self.conversation_1 = conversation
    
    #method for giving gifts to characters to increase their friendliness towards the player
    def give_gift(self, gift):
        if gift == self.soft_spot:
            print("[" + self.name + " says]: " + self.conversation_1)
            self.affinity = 1
            return True
        else:
            print(self.name + " doesn't seem interested in your gift. \n")
            return False
        
    def talk(self):
        if self.conversation_0 is not None:
            if self.affinity == 0:
                print("[" + self.name + " says]: " + self.conversation_0 + "\n")
            else:
                print("[" + self.name + " says]: " + self.conversation_1 + "\n")