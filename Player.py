from Game_character import Game_character

class Player(Game_character):
    def __init__(self, level=None, experience_points=None):
        self.level = level
        self.experience_points = experience_points

    #Creates a getter and setter for the level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    #Creates a getter and setter for the experience points
    @property
    def experience_points(self):
        return self._experience_points

    @experience_points.setter
    def experience_points(self, experience_points):
        self._experience_points = experience_points

    def gain_experience(self, experience):
        self.experience = experience
        self.experience_points = self.experience_points + self.experience
        if self.experience_points == self.level:
            self.level = self.level + self.experience
            self.hit_points = self.hit_points + self.experience
            self.damage_points = self.damage_points + self.experience


def main():
    player = Player()

    player.name = "Percy"
    print(player.name)

    player.hit_points = 60
    print(f"Hit points {player.hit_points}")

    player.damage_points = 10

    player.attack()

    player.attack()

    print(f"Current Hit points is {player.hit_points}")

    player.level = 20
    print(f"Level {player.level}")

    player.experience_points = 15
    print(f"Experience points {player.experience_points}")

    player.gain_experience(5)
    print(f"Level {player.level}")
    print(f"Hit points {player.hit_points}")
    print(f"Damage points {player.damage_points}")


if __name__ == "__main__":
    main()