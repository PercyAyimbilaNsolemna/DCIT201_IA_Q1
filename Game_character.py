class Game_character:
    def __init__(self, name=None, hit_points=None, damage_points=None):
        self.name = name
        self.hit_points = hit_points
        self.damage_points = damage_points

    #Creates a method that is callable by the print function
    def __str__(self):
        return("This is a class for Game Character")
    #Creates a getter method for the name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    #Creates a getter and setter for the hit_points
    @property
    def hit_points(self):
        return self._hit_points
    
    @hit_points.setter
    def hit_points(self, hit_points):
        self._hit_points = hit_points

    #Creates a getter and setter for the damage_points
    @property
    def damage_points(self):
        return self._damage_points
    
    @damage_points.setter
    def damage_points(self, damage_points):
        self._damage_points = damage_points

    #Defines an attack method that subtracts the character's damage points from the hit points
    def attack(self):
        self.hit_points = self.hit_points - self.damage_points 




def main():
    game_character = Game_character()

    print(game_character)

    game_character.name = "Percy"

    print(f"Name: {game_character.name}")

    game_character.hit_points = 50

    print(f"The hit points is {game_character.hit_points}")

    game_character.damage_points = 30

    print(f"Damage points {game_character.damage_points}")

    game_character.attack()

    print(f"The current hit points is {game_character._hit_points}" )



if __name__ == "__main__":
    main()