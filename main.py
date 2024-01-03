from skill import Bloodbound, Tempest
from weapon import Bloodvalor, Zephyr
from hero import Character, Wizard, Knight
from stats import Stats, STR, DEX, CON, INT, WIS

claire = Character("Claire li Britania", 580, 180, 15, 25, 25, Wizard("wind"))
aldric = Character("Sir Aldric of The Ironheart", 940, 100, 35, 20, 15, Knight("blood"))

claire_stats = Stats(STR(2), DEX(5), CON(7), INT(13), WIS(9))
aldric_stats = Stats(STR(11), DEX(6), CON(10), INT(1), WIS(8))

aldric.set_weapon(Bloodvalor())
claire.set_weapon(Zephyr())

aldric.set_stats(aldric_stats)
claire.set_stats(claire_stats)

aldric.set_skill(Bloodbound())
claire.set_skill(Tempest())

aldric.use_ability(claire)
claire.use_ability(aldric)

print(claire.__dict__)
print(aldric.__dict__)