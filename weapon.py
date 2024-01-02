from skill import Skill

weapon_types = {
    'T1': 'Sword', 
    'T2': 'Polearm', 
    'T3': 'Bow', 
    'T4': 'Wand', 
    'T5': 'Axe', 
    'T6': 'Firearm', 
    'T7': 'Gauntlet', 
    'T8': 'Orb', 
    'T9':'Hammer', 
    'T10': 'Unique'
}

class Weapon():
    def __init__(self, name:str, type:str, power:float, ability:classmethod) -> None:
        self.__weapon_name = name
        self.__weapon_type = type
        self.__weapon_power = power
        self.__weapon_ability = ability
        self.__weapon_exp = 0
        self.__weapon_level = 1
    
    def get_weapon_name(self):
        return self.__weapon_name
    
    def get_weapon_type(self):
        return self.__weapon_type

    def get_weapon_power(self):
        return self.__weapon_power
    
    def get_weapon_ability(self):
        return self.__weapon_ability
    
    def get_weapon_exp(self):
        return self.__weapon_exp
    
    def get_weapon_level(self):
        return self.__weapon_level
    
    def enhance_weapon(self, val:float):
        self.__weapon_exp += val

    def use_ability(self, hero:classmethod, target:classmethod):
        if self.get_weapon_ability().getSkillCost() <= hero.getMana():
            hero.setMana(-self.get_weapon_ability().getSkillCost())
            damage = self.get_weapon_power() * self.get_weapon_level() + self.get_weapon_ability().getSkillPower() * self.get_weapon_ability().getSkillLevel()
            if self.get_weapon_ability().getSkillType() == "magical":
                damage -= target.getResistance() * target.getLevel()
            elif self.get_weapon_ability().getSkillType() == "physical":
                damage -= target.getDefense() * target.getLevel()
            print("{} is using {} ability: {} and dealt {} damage to {}".format(
                hero.getName(),
                self.get_weapon_name(),
                self.get_weapon_ability().getSkillName(),
                damage,
                target.getName()
            ))
            print("{} consumed {} mana".format(self.get_weapon_ability().getSkillName(), self.get_weapon_ability().getSkillCost()))
            print(hero.infoMp)
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.getName(), 
                self.get_weapon_ability().getSkillCost(),
                self.get_weapon_name()))
            return
        
class Bloodvalor(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Bloodvalor Reach", weapon_types.get('T2'), 54, Skill.__init__(self, "Ironheart Resilience", 41, 55, "physical"))
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
        damage = self.get_weapon_power() + (self.get_weapon_level() * self.get_weapon_power() * self.getAbilityGrowth()) + (self.getSkillPower() * self.getSkillLevel())
        return damage

    def getAbilityShield(self):
        shield = self.getShieldBuff() + (self.getShieldBuff() * self.getShieldMultiplier())
        return shield
    
    def use_ability(self, hero:classmethod, target:classmethod):
        damage = self.getAbilityDamage() - target.getDefense() * target.getLevel()
        if damage <= 0:
            damage = 0
            return
        
        if self.getSkillCost() <= hero.getMana():
            hero.setMana(-self.getSkillCost())
            hero.addShield(self.getAbilityShield())
            print("{} casted Ironheart Resilience, create {} points of shield".format(
                hero.getName(),
                self.getAbilityShield()
            ))
            print("{} exude a heavy, bloodlusted aura, dealing {} damage to {}".format(
                hero.getName(),
                damage,
                target.getName()
            ))
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.getName(), 
                self.get_weapon_ability().getSkillCost(),
                self.get_weapon_name()))
            return

class Zephyr(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Zephyr Embrace", weapon_types.get('T4'), 87, Skill.__init__(self, "Galeweave", 73, 82, "magical"))
        self.__buff_multiplier = 0.5
        self.__buff_growth = 1
        self.__damage_growth = 0.2

    def getAbilityGrowth(self):
        return self.__damage_growth

    def getAbilityDamage(self):
        damage = self.get_weapon_power() + (self.get_weapon_level() * self.get_weapon_power() * self.getAbilityGrowth()) + (self.getSkillPower() * self.getSkillLevel())
        return damage
    
    def getAttackBuff(self):
        buff = self.__buff_multiplier * self.get_weapon_power()
        buff += self.__buff_growth * buff
        return buff

    def use_ability(self, hero:classmethod, target:classmethod):
        damage = self.getAbilityDamage() - target.getResistance() * target.getLevel()
        if damage <= 0:
            damage = 0
            return
    
        if self.getSkillCost() <= hero.getMana():
            hero.setMana(-self.getSkillCost())
            hero.setAttackPower(self.getAttackBuff())
            print("{} casted Galeweave, increased {} points of attack".format(
                hero.getName(),
                self.getAttackBuff()
            ))
            print("By the grace of the wind, {} summons a wind vortex, dealing {} damage tp {}".format(
                hero.getName(),
                damage,
                target.getName()
            ))
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.getName(), 
                self.get_weapon_ability().getSkillCost(),
                self.get_weapon_name()))
            return