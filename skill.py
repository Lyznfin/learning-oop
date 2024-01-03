from enum import Enum

class Skill_Type(Enum):
    T1 = 'physical'
    T2 = 'magical'
    T3 = 'divine'
    T4 = 'hybrid'
    T5 = 'true'

class Skill():
    def __init__(self, name:str, power:float, cost:float, type:str) -> None:
        self.__skill_name = name
        self.__skill_power = power
        self.__skill_cost = cost
        self.__skill_type = type
        self.__skill_exp = 0
        self.__skill_level = 1

    def get_skill_name(self):
        return self.__skill_name
    
    def get_skill_power(self):
        return self.__skill_power
    
    def get_skill_cost(self):
        return self.__skill_cost
    
    def get_skill_type(self):
        return self.__skill_type
    
    def get_skill_proficiency(self):
        return self.__skill_exp
    
    def get_skill_level(self):
        return self.__skill_level
    
    def gain_skill_proficiency(self, value:float):
        self.__skill_exp += value
    
    def level_up_skill(self):
        self.__skill_level += 1
        return
    
    def use_skill(self):
        pass
    
class Bloodbound(Skill):
    def __init__(self) -> None:
        super().__init__("Bloodbound Vengeance", 126, 75, Skill_Type.T1.value)
        self.__buff = 1.5
        self.__buff_growth = 1
        self.__power_growth = 0.2
    
    def get_buff(self):
        return self.__buff
    
    def get_buff_growth(self):
        return self.__buff_growth
    
    def get_power_growth(self):
        return self.__power_growth
    
    def get_buff_defense(self):
        return self.__buffDefense
    
    def get_buff_resistance(self):
        return self.__buffResistance
        
    def use_skill(self, hero:classmethod, target:classmethod):
        self.gain_skill_proficiency(50 + 12 * target.getLevel())
        hero.update_mana(-self.get_skill_cost())
        multiplier = self.get_skill_level() * self.get_buff_growth() + self.get_buff()
        self.__buffDefense = multiplier * hero.get_defense() - hero.get_defense()
        self.__buffResistance = multiplier * hero.get_resistance() - hero.get_resistance()
        print("{} has used {}, defences and resistances has been increased by {} and {} points".format(
            hero.get_name(),
            self.get_skill_name(),
            self.get_buff_defense(),
            self.get_buff_resistance()
        ))
        hero.update_defense(self.get_buff_defense())
        hero.update_resistance(self.get_buff_resistance())
        damage = self.get_skill_power() + (self.get_skill_power() * self.get_skill_level())
        damage = damage + damage * self.get_power_growth()
        damage -= target.get_defense() * target.get_level()
        print("{} has infused his spear with an intensified blood aura, deals {} {} damage to {}".format(
            hero.get_name(),
            damage,
            self.get_skill_type(),
            target.get_name()
        ))
        print("{} consumed {} mana".format(self.get_skill_name(), self.get_skill_cost()))
        print(hero.infoMp)
        target.attacked(hero, damage)
    
    def buff_ended(self, hero:classmethod):
        print("{} duration has ended".format(self.get_skill_name()))
        hero.update_defense(-self.get_buff_defense())
        hero.update_resistance(-self.get_buff_resistance())

class Tempest(Skill):
    def __init__(self) -> None:
        super().__init__("Tempest Razorslash", 62, 95, Skill_Type.T2.value)
        self.__power_growth = 0.2
        self.__consecutive_attack = 3
    
    def get_power_growth(self):
        return self.__power_growth
    
    def get_consecutive_attack(self):
        return self.__consecutive_attack
    
    def use_skill(self, hero:classmethod, target:classmethod):
        self.gain_skill_proficiency(50 + 12 * target.get_level())
        hero.update_mana(-self.get_skill_cost())
        damage = self.get_skill_power() + (self.get_skill_power() * self.get_skill_level() * self.get_power_growth())
        damage -= target.get_resistance() * target.get_level()
        print("{} unleashed {}".format(
                hero.get_name(),
                self.get_skill_name()
        ))
        for _ in range(self.get_consecutive_attack()):
            print("The bursts of wind deals {} {} damage to {}".format(
                round(damage, 1),
                self.get_skill_type(),
                target.get_name()
            ))
        print("{} consumed {} mana".format(self.get_skill_name(), self.get_skill_cost()))
        print(hero.infoMp)
        target.attacked(hero, round(damage * self.get_consecutive_attack(), 1))