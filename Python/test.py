from LOTR.orc import Orc
from LOTR.knight import Knight
from LOTR.archer import Archer

import shelve

""" TESTING """


def to_file(object):
    if object is None:
        return 0
    testFile = object.get_class_name() + object.getName()
    db = shelve.open(testFile)
    instance = object
    db[object.getName()] = instance
    db.close()


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

player2.battle(player3)  # test orc(no weapon) vs orc(no weapon)
player1.battle(player2)  # test orc(weapon) vs orc(no weapon)
player2.battle(player5)  # test orc(no weapon) vs human(weapon)
player4.battle(player3)  # test knight(weapon) vs orc(weapon)
player3.battle(player8)  # test orc(no weapon) vs archer(weapon)
player8.battle(player9)  # test archer(weapon) vs archer(weapon)
