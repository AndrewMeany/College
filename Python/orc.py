from LOTR.fighter import Fighter

""" ORC CLASS (LVL2) """


class Orc(Fighter):
    def __init__(self, name, skill, strength, weapon=False):
        Fighter.__init__(self, name, skill, weapon)
        if strength <= 0:
            print("Strength Error: Please enter a value greater than 0.")
            exit()
        else:
            self._strength = float(strength)

    def setStrength(self, strength):
        if strength <= 0:
            print("Strength Error: Please enter a value greater than 0.")
        else:
            self._strength = float(strength)

    def getStrength(self):
        return self._strength

    strength = property(getStrength, setStrength)

    def __str__(self):
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Strength Level: {self._strength:.2f} | Weapon: {self._weapon}"

    def __gt__(self, opponent):
        winner = 0
        if self._weapon is False:
            if opponent.getWeapon() is False:
                if self._strength > opponent.getStrength():
                    winner = 0
                elif self._strength < opponent.getStrength():
                    winner = 1
            else:
                if opponent.getWeapon() is False:
                    winner = 0
                else:
                    if self._skill > opponent.getSkill():
                        winner = 0
                    elif self._skill < opponent.getSkill():
                        winner = 1
        return winner

    def battle(self, opponent):
        winner = self > opponent
        if winner == 0:
            self.setSkill(self._skill * 1.05)
            print(f"{self._name} has won the battle! Their skill level has increased by 5% to {self._skill:.2f}.")
            return self
        elif winner == 1:
            opponent.setSkill(opponent.getSkill() * 1.05)
            print(
                f"{opponent.getName()} has won the battle! Their skill level has increased by 5% to {opponent.getSkill():.2f}.")
            return opponent
        else:
            print("Both combatants lose!")
            return None
