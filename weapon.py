from skill import Skill

class Weapon():
    def __init__(self, name:str, power:float, ability:classmethod) -> None:
        self.__weapon_name = name
        self.__weapon_power = power
        self.__weapon_ability = ability
        self.__weapon_exp = 0
        self.__weapon_level = 1
    
    def getWeaponName(self):
        return self.__weapon_name
    
    def getWeaponPower(self):
        return self.__weapon_power
    
    def getWeaponAbility(self):
        return self.__weapon_ability
    
    def getWeaponExp(self):
        return self.__weapon_exp
    
    def getWeaponLevel(self):
        return self.__weapon_level
    
    def enhanceWeapon(self):
        self.__weapon_level += 1

    def useAbility(self, hero:classmethod, target:classmethod):
        if self.getWeaponAbility().getSkillCost() <= hero.getMana():
            hero.setMana(-self.getWeaponAbility().getSkillCost())
            damage = self.getWeaponPower() * self.getWeaponLevel() + self.getWeaponAbility().getSkillPower() * self.getWeaponAbility().getSkillLevel()
            if self.getWeaponAbility().getSkillType() == "magical":
                damage -= target.getResistance() * target.getLevel()
            elif self.getWeaponAbility().getSkillType() == "physical":
                damage -= target.getDefense() * target.getLevel()
            print("{} is using {} ability: {} and dealt {} damage to {}".format(
                hero.getName(),
                self.getWeaponName(),
                self.getWeaponAbility().getSkillName(),
                damage,
                target.getName()
            ))
            print("{} consumed {} mana".format(self.getWeaponAbility().getSkillName(), self.getWeaponAbility().getSkillCost()))
            print(hero.infoMp)
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.getName(), 
                self.getWeaponAbility().getSkillCost(),
                self.getWeaponName()))
            return
        
class Bloodvalor(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Bloodvalor Reach", 54, Skill.__init__(self, "Ironheart Resilience", 41, 55, "physical"))
        self.__shield_buff = 100
        self.__shield_multiplier = 0.5
        self.__damage_growth = 0.2

    def getAbilityGrowth(self):
        return self.__damage_growth
    
    def getShieldBuff(self):
        return self.__shield_buff
    
    def getShieldMultiplier(self):
        return self.__shield_multiplier * self.getSkillLevel()
    
    def getAbilityDamage(self):
        damage = self.getWeaponPower() + (self.getWeaponLevel() * self.getWeaponPower() * self.getAbilityGrowth()) + (self.getSkillPower() * self.getSkillLevel())
        return damage

    def getAbilityShield(self):
        shield = self.getShieldBuff() + (self.getShieldBuff() * self.getShieldMultiplier())
        return shield
    
    def useAbility(self, hero:classmethod, target:classmethod):
        damage = self.getAbilityDamage() - target.getDefense() * target.getLevel()
        if damage <= 0:
            damage = 0
            return
        
        if self.getSkillCost() <= hero.getMana():
            hero.setMana(-self.getSkillCost())
            hero.addShield(self.getAbilityShield())
            print("{} casted Ironheart Resilience, create {} points of shield and dealt {} damage to {}".format(
                hero.getName(),
                self.getAbilityShield(),
                damage,
                target.getName()
            ))
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.getName(), 
                self.getWeaponAbility().getSkillCost(),
                self.getWeaponName()))
            return

class Zephyr(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Zephyr Embrace", 87, Skill.__init__(self, "Galeweave", 73, 82, "magical"))

    def useAbility(self, hero:classmethod, target:classmethod):
        pass