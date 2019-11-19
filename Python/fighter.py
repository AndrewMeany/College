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
