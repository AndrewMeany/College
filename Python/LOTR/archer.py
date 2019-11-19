from LOTR.human import Human

""" ARCHER CLASS (LVL3) """


class Archer(Human):
    def __init__(self, name, skill, kingdom, weapon=True):
        Human.__init__(self, name, skill, kingdom, weapon)

    @property
    def __str__(self):
        return f"Name: {self._name} | Skill Level: {self._skill:.2f} | Kingdom: {self._kingdom} | Weapon: {self._weapon}"
