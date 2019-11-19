from LOTR.human import Human

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
