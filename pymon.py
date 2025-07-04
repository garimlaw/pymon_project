class Location:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.door = {"west": None, "north": None, "east": None, "south": None}
        self.creatures = []
        self.items = []

class Creature:

    def __init__(self, name, description, location):
/*************  ✨ Windsurf Command ⭐  *************/
        """
        Constructor for Creature object
        
        Parameters:
        name (str): name of the creature
        description (str): description of the creature
        location (Location): location of the creature
        """
/*******  29fcbc81-3aa7-4220-ab68-b9b6688e0eb8  *******/
        self.name = name
        self.description = description
        self.location = location 
        ##git check

    

