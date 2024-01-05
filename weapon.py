from skill import Skill, Skill_Type
from enum import Enum
from stats import Stats, STR, DEX, CON, INT, WIS


class Weapon_Types(Enum):
    T1 = 'Sword'
    T2 = 'Polearm'
    T3 = 'Bow'
    T4 = 'Wand'
    T5 = 'Axe'
    T6 = 'Firearm'
    T7 = 'Gauntlet'
    T8 = 'Orb'
    T9 = 'Hammer'
    T10 = 'Unique'

valid_weapon_types = {item.value for item in Weapon_Types}

class Weapon_Handed(Enum):
    H0 = '0-Handed'
    H1 = '1-Handed'
    H2 = '2-Handed'

valid_weapon_handed = {item.value for item in Weapon_Handed}

class Weapon:
    def __init__(self, name:str, type:str, power:float, ability:classmethod) -> None:
        assert type in valid_weapon_types, "Invalid Weapon Type"
        assert isinstance(name, str) and name.strip(), "Name cannot be empty or None"
        assert isinstance(power, (float, int)) and power > 0, "Power should be a positive number"
        self.__weapon_name = name
        self.__weapon_type = type
        self.__weapon_handed = None
        self.__weapon_scaling = None
        self.__weapon_requirement = None
        self.__weapon_base_power = power
        self.__weapon_ability = ability
        self.__weapon_exp = 0
        self.__weapon_level = 1
    
    def get_weapon_name(self):
        return self.__weapon_name
    
    def get_weapon_type(self):
        return self.__weapon_type

    def get_weapon_handed(self):
        return self.__weapon_handed
    
    def get_weapon_scaling(self, attribute:str):
        #contoh scaling ajh, pake dictionary cuy
        self.__weapon_scaling = {
            'STR': 0.05, #Ini ganti aja 'S'nya pake angka. Word kek 'A', 'S', dkk buat kerenan aja
            'DEX': 0.02, #Nanti pake treshold angka, kek misal scaling range(1, 1.1) = E, range(1.1, 1.3) = D, dll gitu
            'CON': None,
            'INT': None,
            'WIS': None            
            }
        
        #Ini dia, goated dict
        return self.__weapon_scaling.get(attribute)
    
    def get_weapon_requirement(self, stats:classmethod):
        return self.__weapon_requirement

    def set_weapon_power(self, stats, **kwargs):
        weapon_power = self.get_weapon_base_power()
        i = 0
        while i < len(kwargs['stat']):
            match kwargs['stat'][i]:
                case 'STR':
                    weapon_power += 0.2 * weapon_power * (stats.get_STR().get_ammount() * self.get_weapon_scaling(kwargs['stat'][i]))
                case 'DEX':
                    weapon_power += 0.2 * weapon_power * (stats.get_DEX().get_ammount() * self.get_weapon_scaling(kwargs['stat'][i]))
                case 'CON':
                    weapon_power += 0.2 * weapon_power * (stats.get_CON().get_ammount() * self.get_weapon_scaling(kwargs['stat'][i]))
                case 'INT':
                    weapon_power += 0.2 * weapon_power * (stats.get_INT().get_ammount() * self.get_weapon_scaling(kwargs['stat'][i]))
                case 'WIS':
                    weapon_power += 0.2 * weapon_power * (stats.get_WIS().get_ammount() * self.get_weapon_scaling(kwargs['stat'][i]))
                case _:
                    return f'Invalid keyword argument'
            i += 1
        return f'{weapon_power}'

    def get_weapon_base_power(self):
        return self.__weapon_base_power
    
    def get_weapon_ability(self):
        return self.__weapon_ability
    
    def get_weapon_exp(self):
        return self.__weapon_exp
    
    def get_weapon_level(self):
        return self.__weapon_level
    
    def enhance_weapon(self, val:float):
        self.__weapon_exp += val

    def use_ability(self, hero:classmethod, target:classmethod):
        pass

class Bloodvalor(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Bloodvalor Reach", Weapon_Types.T2.value, 54, Skill.__init__(self, "Ironheart Resilience", 41, 55, Skill_Type.T1.value))
        self.__shield_buff = 100
        self.__shield_multiplier = 0.5
        self.__damage_growth = 0.2

    def get_ability_growth(self):
        return self.__damage_growth
    
    def get_shield_buff(self):
        return self.__shield_buff
    
    def get_shield_multiplier(self):
        return self.__shield_multiplier * self.get_skill_level()
    
    def get_ability_damage(self):
        damage = self.get_weapon_base_power() + (self.get_weapon_level() * self.get_weapon_base_power() * self.get_ability_growth()) + (self.get_skill_power() * self.get_skill_level())
        return damage

    def get_ability_shield(self):
        shield = self.get_shield_buff() + (self.get_shield_buff() * self.get_shield_multiplier())
        return shield
    
    def use_ability(self, hero:classmethod, target:classmethod):
        damage = self.get_ability_damage() - target.get_defense() * target.get_level()
        if damage <= 0:
            damage = 0
            return
        
        if self.get_skill_cost() <= hero.get_mana():
            hero.update_mana(-self.get_skill_cost())
            hero.set_shield(self.get_ability_shield())
            print("{} casted Ironheart Resilience, create {} points of shield".format(
                hero.get_name(),
                self.get_ability_shield()
            ))
            print("{} exude a heavy, bloodlusted aura, dealing {} damage to {}".format(
                hero.get_name(),
                damage,
                target.get_name()
            ))
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.get_name(), 
                self.get_weapon_ability().get_skill_cost(),
                self.get_weapon_name()))
            return

class Zephyr(Weapon, Skill):
    def __init__(self) -> None:
        super().__init__("Zephyr Embrace",  Weapon_Types.T4.value, 87, Skill.__init__(self, "Galeweave", 73, 82, Skill_Type.T2.value))
        self.__buff_multiplier = 0.25
        self.__buff_growth = 0.5
        self.__damage_growth = 0.2

    def get_ability_growth(self):
        return self.__damage_growth

    def get_ability_damage(self):
        damage = self.get_weapon_base_power() + (self.get_weapon_level() * self.get_weapon_base_power() * self.get_ability_growth()) + (self.get_skill_power() * self.get_skill_level())
        return damage
    
    def get_attack_buff(self):
        buff = self.__buff_multiplier * self.get_weapon_base_power()
        buff += self.__buff_growth * buff
        return buff

    def use_ability(self, hero:classmethod, target:classmethod):
        damage = self.get_ability_damage() - target.get_resistance() * target.get_level()
        if damage <= 0:
            damage = 0
            return
    
        if self.get_skill_cost() <= hero.get_mana():
            hero.update_mana(-self.get_skill_cost())
            hero.set_attack_power(self.get_attack_buff())
            print("{} casted Galeweave, increased {} points of attack".format(
                hero.get_name(),
                self.get_attack_buff()
            ))
            print("By the grace of the wind, {} summons a wind vortex, dealing {} damage tp {}".format(
                hero.get_name(),
                damage,
                target.get_name()
            ))
            target.attacked(hero, damage)
        else:
            print(hero.infoMp)
            print("{} mana is less than {}, cannot use {} ability".format(
                hero.get_name(), 
                self.get_weapon_ability().getSkillCost(),
                self.get_weapon_name()))
            return
        
a = Weapon('Test', 'Sword', 50, None)
weap_stat = Stats(STR(15), DEX(19), CON(12), INT(21), WIS(12))
print(a.set_weapon_power(weap_stat, stat=['STR', 'DEX']))