from skill import Bloodbound, Tempest
from weapon import Bloodvalor, Zephyr
from hero import Character, Wizard, Knight
from stats import Stats, STR, DEX, CON, INT, WIS

claire = Character("Claire li Britania", 580, 180, 15, 25, 25, Wizard("wind"))
aldric = Character("Sir Aldric of The Ironheart", 940, 100, 35, 20, 15, Knight("blood"))

claire_stats = Stats(STR(2), DEX(5), CON(7), INT(13), WIS(9))

aldric.setWeapon(Bloodvalor())
claire.setWeapon(Zephyr())

aldric.setSkill(Bloodbound())
claire.setSkill(Tempest())

aldric.useWeaponAbility(aldric, claire)
claire.useWeaponAbility(claire, aldric)

print(claire.__dict__)
print(aldric.__dict__)