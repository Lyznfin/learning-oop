from skill import Skill, Bloodbound, Tempest
from weapon import Weapon, Bloodvalor, Zephyr 
from hero import Character, Wizard, Knight

Claire = Character("Claire li Britania", 580, 180, 15, 25, 25, Wizard("wind"))
Aldric = Character("Sir Aldric of The Ironheart", 940, 100, 35, 20, 15, Knight("blood"))

Aldric.setWeapon(Bloodvalor())
Claire.setWeapon(Zephyr())

Aldric.setSkill(Bloodbound())
Claire.setSkill(Tempest())

Aldric.useWeaponAbility(Aldric, Claire)
Claire.useWeaponAbility(Claire, Aldric)

print(Claire.__dict__)
print(Aldric.__dict__)

game = True

while game != False:
    pass