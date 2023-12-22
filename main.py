from skill import Skill, Bloodbound, Tempest
from weapon import Weapon, Bloodvalor 
from hero import Hero, Mage, Fighter

Claire = Hero("Claire li Britania", 580, 180, 15, 25, 21, Mage("wind"))
Aldric = Hero("Sir Aldric of The Ironheart", 940, 100, 35, 20, 14, Fighter("blood"))

Staff = Weapon("Zephyr Embrace", 87, Skill("Galeweave", 73, 82, "magical"))

Aldric.setWeapon(Bloodvalor())
Claire.setWeapon(Staff)

Aldric.setSkill(Bloodbound())
Claire.setSkill(Tempest())

Aldric.getWeapon().useWeaponAbility(Aldric, Claire)
Claire.attack(Aldric)
Claire.attack(Aldric)
Claire.attack(Aldric)
Claire.attack(Aldric)
Claire.attack(Aldric)

print(Claire.__dict__)
print(Aldric.__dict__)