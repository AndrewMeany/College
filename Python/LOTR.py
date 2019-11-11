""" GENERAL (LVL1) CLASS """


class Fighter(object):
    def __init__(self, name, skill, weapon=False):
        if not name.isalpha():
            print("Name Error: Please use letters only.")
            exit()
        else:
            self._name = str(name)
        if skill <= 0:
            print("Skill Error: Please enter a value greater than 0.")
            exit()
        else:
            self._skill = float(skill)
        self._weapon = bool(weapon)

    def setName(self, name):
        if not name.isalpha():
            print("Name Error: Please use letters only.")
        else:
            self._name = str(name)

    def getName(self):
        return self._name

    def setSkill(self, skill):
        if skill <= 0:
            print("Skill Error: Please enter a value greater than 0.")
        else:
            self._skill = float(skill)

    def getSkill(self):
        return self._skill

    def setWeapon(self, weapon):
        if weapon is True:
            print(f"Hurrah! {self._name} now has a weapon!")
        elif weapon is False:
            print(f"Uh oh! {self._name} now has no weapon!")
        self._weapon = bool(weapon)

    def getWeapon(self):
        return self._weapon

    def getClass(self):
        return self.__class__.__name__

    name = property(getName, setName)
    skill = property(getSkill, setSkill)
    weapon = property(getWeapon, setWeapon)

    def __str__(self):
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Weapon: {self._weapon}"

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


""" KNIGHT CLASS (LVL3) """


class Knight(Human):
    def __init__(self, name, skill, kingdom, squad, weapon=True):
        Human.__init__(self, name, skill, kingdom, weapon)
        self._squad = squad

    def getSquad(self):
        return self._squad

    def setSquad(self, squad):
        self._squad = squad

    squad = property(getSquad, setSquad)

    def __str__(self):
        squad = "Squad:"
        if len(self._squad) == 0:
            squad += ' None'
        else:
            for ally in self._squad:
                squad += (" " + ally.getName())
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Kingdom: {self._kingdom} | " + squad + f"| Weapon: {self._weapon}"


""" ARCHER CLASS (LVL3) """


class Archer(Human):
    def __init__(self, name, skill, kingdom, weapon=True):
        Human.__init__(self, name, skill, kingdom, weapon)

    def __str__(self):
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Kingdom: {self._kingdom} | Weapon: {self._weapon}"


""" TESTING """

print("\n- Create Players -")

player1 = Orc("Azog", 9, 9.5, False)  # create orc player1
print(player1)  # print player1 str
player1.name = "Balcmeg"  # change orc player1 name
player1.skill = 4  # change orc player1 skill level
player1.weapon = True  # change orc player1 weapon status to true
print(player1)  # print player1 str

player2 = Orc("Snaga", 13.6, 18.7, False)  # create orc player2
print(player2)  # print player2 str

player3 = Orc("Golfimbul", 12.2, 14.8, False)  # create orc player3
print(player3)  # print player3 str

player4 = Orc("Snaga", 7.7, 21, True)  # create orc player4
print(player4)  # print player4 str

player7 = Archer("RohirrimArcherA", 18, "Rohan", True)
player8 = Archer("RohirrimArcherB", 15, "Rohan", True)
player9 = Archer("RohirrimArcherC", 19, "Rohan", True)
player10 = Archer("RohirrimArcherD", 20, "Rohan", True)
player11 = Archer("RohirrimArcherE", 12, "Rohan", True)

squad1 = [player7, player8]
squad2 = [player9, player10]

player5 = Knight("Boromir", 30, "Mordor", squad1, False)  # create human player5 + test for no weapon
player5.skill = 25  # change human player5 skill level
player5.kingdom = "Gondor"  # change human player5 kingdom name
player5.weapon = True  # change human player5 weapon status to true
print(player5)  # print player5 str

player6 = Knight("Aragorn", 37, "Rivendell", squad2, True)  # create human player6
print(player6)  # print player6 str

print("\n- Battles- ")  # begin battle testing

Fighter.battle(player2, player3)  # test orc(no weapon) vs orc(no weapon)
Fighter.battle(player1, player2)  # test orc(weapon) vs orc(no weapon)
Fighter.battle(player2, player5)  # test orc(no weapon) vs human(weapon)
Fighter.battle(player4, player3)  # test knight(weapon) vs orc(weapon)
Fighter.battle(player3, player8)  # test orc(no weapon) vs archer(weapon)
Fighter.battle(player8, player9)  # test archer(weapon) vs archer(weapon)
