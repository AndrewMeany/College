from LOTR.fighter import Fighter

""" HUMAN CLASS (LVL2) """


class Human(Fighter):
    def __init__(self, name, skill, kingdom, weapon=True):
        Fighter.__init__(self, name, skill, weapon)
        if kingdom == "":
            print("To which kingdom does this player swear allegiance?")
            exit()
        elif not kingdom.isalpha():
            print("Kingdom Error: Please use letters only.")
            exit()
        else:
            self._kingdom = str(kingdom)
        if self._weapon is False:
            print("A human cannot fight without a weapon!")
        else:
            self._weapon = weapon

    def getKingdom(self):
        return self._kingdom

    def setKingdom(self, kingdom):
        if kingdom == "":
            print("To which kingdom does this player swear allegiance?")
            exit()
        elif not kingdom.isalpha():
            print("Kingdom Error: Please use letters only.")
            exit()
        else:
            self._kingdom = kingdom

    def setWeapon(self, weapon):
        if self._weapon is False:
            print("A human cannot fight without a weapon!")
        else:
            self._weapon = weapon

    kingdom = property(getKingdom, setKingdom)

    def __str__(self):
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Kingdom: {self._kingdom} | Weapon: {self._weapon}"

    def __gt__(self, opponent):
        winner = 0
        if opponent.__class__.__name__ != "Orc":
            print("Humans should keep the fighting to the orcs!")
            exit()
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
