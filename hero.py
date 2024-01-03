from abc import ABC, abstractmethod
from enum import Enum

class Character():
    def __init__(self, name:str, hp:float, mp:float, ap:float, role:classmethod) -> None:
        self.__name = name
        self.__max_health = hp
        self.__health = self.get_max_health()
        self.__max_mana = mp
        self.__mana = self.get_max_mana()
        self.__attack_power = ap
        self.__shield = 0
        self.__exp = 0
        self.__level = 1
        self.__isAlive = True
        self.__role = role
        self.__exp_treshold = self.get_level() * 2 * 50

    def set_stats(self, stats:classmethod):
        self.__stats = stats
        self.initialize_stats()

    def get_stats(self):
        return self.__stats

    def initialize_stats(self):
        self.set_defense()
        self.set_resistance()

    def get_name(self):
        return self.__name
    
    def get_max_health(self):
        return self.__max_health

    def get_health(self):
        return self.__health
    
    def set_health(self, value:float):
        self.__health = value

    def update_health(self, value:float):
        self.__health += value
    
    def get_max_mana(self):
        return self.__max_mana

    def get_mana(self):
        return self.__mana
    
    def set_mana(self, value:float):
        self.__mana = value

    def update_mana(self, value:float):
        self.__mana += value

    def set_defense(self):
        self.__defense = self.get_stats().get_defense()

    def get_defense(self):
        return self.__defense
    
    def update_defense(self, value:float):
        self.__defense += value

    def set_resistance(self):
        self.__resistance = self.get_stats().get_resistance()

    def get_resistance(self):
        return self.__resistance
    
    def update_resistance(self, value:float):
        self.__resistance += value

    def get_attack_power(self):
        return self.__attack_power
    
    def set_attack_power(self, value:float):
        self.__attack_power += value
    
    def get_status(self):
        return self.__isAlive
    
    def get_exp(self):
        return self.__exp
    
    def get_exp_treshold(self):
        return self.__exp_treshold
    
    def set_exp_treshold(self):
        self.__exp_treshold = self.get_level() * 2 * 50
    
    def get_level(self):
        return self.__level
    
    def get_role(self):
        return self.__role
    
    def set_weapon(self, weapon:classmethod):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def set_skill(self, skill:classmethod):
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def get_shield(self):
        return self.__shield
    
    def set_shield(self, value:float):
        self.__shield = value

    def add_shield(self, value:float):
        self.__shield += value

    def attack(self, target:classmethod):
        if not self.get_status():
            print("{} is dead, cannot attack".format(self.get_name()))
            return
        if not target.get_status():
            print("{} is dead, cannot be attacked".format(target.get_name()))
            return
        elif self.get_role().get_mana_cost() > self.get_mana():
            print(self.infoMp)
            print("{} mana is less than {}, cannot cast a basic spell".format(self.get_name(), self.get_role().get_mana_cost()))
            return
        else:
            return self.get_role().attack(self, target)
        
    def use_skill(self, target:classmethod):
        if not self.get_status():
            print("{} is dead, cannot attack".format(self.get_name()))
            return
        elif not target.get_status():
            print("{} is dead, cannot be attacked".format(target.get_name()))
            return
        if self.get_skill().get_skill_cost() > self.get_mana():
            print(self.infoMp)
            print("{} doesnt have enough mana to use skill: {}".format(
                self.get_name(),
                self.get_skill().get_name()
            ))
            return
        else:
            self.get_skill().use_skill(self, target)
        
    def use_ability(self, target:classmethod):
        if not self.get_status():
            print("{} is dead, cannot use ability".format(self.get_name()))
            return
        elif not target.get_status():
            print("{} is dead, cannot be attacked".format(target.get_name()))
            return
        else:
            return self.get_weapon().use_ability(self, target)

    def reduce_damage(self, damage:int):
        if damage <= self.get_shield() and self.get_shield() != 0:
            print('{} points damage has completely been absorbed'.format(damage, self.get_name()))
            self.add_shield(-damage)
            damage = 0
            print('{} has {} points of shield left'.format(self.get_name(), self.get_shield()))
        elif damage > self.get_shield() and self.get_shield() != 0:
            absorbed = damage
            damage -= self.get_shield() 
            absorbed -= damage
            print('{} points of damage has been absorbed'.format(absorbed))
            print('{} shields is now completely gone'.format(self.get_name()))
            self.set_shield(0)
        return damage

    def attacked(self, attacker:classmethod, damage:classmethod):
        if self.get_shield() > 0:
            damage = self.reduce_damage(damage)
        self.update_health(-round(damage))
        if damage <= 0:
            print('No ammount of damage is dealt to {}'.format(self.get_name()))
            damage = 0
            return
        else:
            print("{} health has decreased by {} points".format(self.get_name(), damage))
            if self.get_health() <= 0:
                self.hero_died()
                expGain = (self.get_exp() / 2) + 50
                attacker.set_exp(expGain)
                return
            else:
                print(self.infoHp)

    def set_exp(self, exp:float):
        self.__exp += exp
        if self.get_exp() >= self.get_exp_treshold():
            self.level_up()

    def level_up(self):
        if self.get_level() % 5 == 0:
            print("{} has reached level {}, you can choose a skill based on you role of {} {}!".format(
                self.get_name(),
                self.get_level(),
                self.get_role().getType(),
                self.get_role().getRole()
            ))
            return
        else:
            self.set_exp(-self.get_exp_treshold())
            self.__attack_power += self.get_role().getAttackGrowth() * self.get_level()
            self.__max_health += self.get_role().getHealthGrowth() * self.get_level()
            self.__max_mana += self.get_role().getManaGrowth() * self.get_level()
            self.update_defense(self.get_role().getDefenseGrowth() * self.get_level())
            self.update_resistance(self.get_role().getResistanceGrowth() * self.get_level())
            self.__level += 1
            self.restore_stat()
            print("{} has leveled up".format(self.get_name()))
            self.set_exp_treshold()
            self.level_up()
        return

    def restore_stat(self):
        self.__health = self.get_max_health()
        self.__mana = self.get_max_mana()

    def hero_died(self):
        self.__health = 0
        self.__mana = 0
        self.__isAlive = False
        self.__exp /= 2
        print("{} has died".format(self.get_name()))

    def respawn(self):
        self.restore_stat()
        self.__isAlive = True

    def regen(self):
        health_regen = self.get_role().getHealthRegen() * self.get_level()
        mana_regen = self.get_role().getManaRegen() * self.get_level()

        if health_regen + self.get_health() >= self.get_max_health():
            health_regen = self.get_max_health() - self.get_health()
            self.update_health(health_regen)
        else:
            self.update_health(health_regen)
        
        if mana_regen + self.get_mana() >= self.get_max_mana():
            mana_regen = self.get_max_mana() - self.get_mana()
            self.update_mana(mana_regen)
        else:
            self.update_mana(mana_regen)

    @property
    def infoHp(self):
        if self.get_status():
            return "{} has {}/{} health left".format(
                self.get_name(), 
                self.get_health(), 
                self.get_max_health(), 
                )
        else:
            return "{} is dead".format(
                self.get_name()
            )
    
    @property
    def infoMp(self):
        if self.get_mana() > 0:
            return "{} has {}/{} mana left".format(
                self.get_name(), 
                self.get_mana(), 
                self.get_max_mana()
                )
        else:
            return "{} has no mana left".format(
                self.get_name()
            )
    
    @property
    def infoExp(self):
        return "{} needs {}/{} exp to level up".format(
            self.get_name(), 
            self.get_exp(),
            self.get_exp() * (self.get_level() * 2)
            )

class Role(ABC):
    @abstractmethod
    def attack(self, hero:Character, target:Character):
        pass

class Element(Enum):
    EA1 = 'Fire'
    EA2 = 'Water'
    EA3 = 'Earth'
    EA4 = 'Air'
    EA5 = 'Lightning'
    EA6 = 'Ice'
    EA7 = 'Light'
    EA8 = 'Dark'
    EA9 = 'Blood'
    EA10 = 'Metal'
    EA11 = 'Mystic'
    EA12 = 'Sound'
    EA13 = 'Time'
    EA14 = 'Gravity'
    EA15 = 'Chaos'
    EA16 = 'Space'

class Wizard(Role):
    def __init__(self, element) -> None:
        self.__role = "magician"
        self.__element = element
        self.__attack_type = "magical"
        self.__attack_growth = 13
        self.__health_growth = 80
        self.__mana_growth = 120
        self.__defense_growth = 2
        self.__resistance_growth = 5
        self.__mana_cost = 35
        self.__health_regen = 2
        self.__mana_regen = 3

    def get_role(self):
        return self.__role
    
    def get_type(self):
        return self.__element

    def get_attack_type(self):
        return self.__attack_type
    
    def get_attack_growth(self):
        return self.__attack_growth
    
    def get_health_growth(self):
        return self.__health_growth
    
    def get_mana_growth(self):
        return self.__mana_growth
    
    def get_defense_growth(self):
        return self.__defense_growth
    
    def get_resistance_growth(self):
        return self.__resistance_growth
    
    def get_mana_cost(self):
        return self.__mana_cost
    
    def get_health_regen(self):
        return self.__health_regen
    
    def get_mana_regen(self):
        return self.__mana_regen

    def attack(self, hero: Character, target: Character):
        damage_multiplier = 0.5 + hero.get_level() / target.get_level()
        damage = hero.get_weapon().getWeaponPower() * 0.5 + (hero.get_attack_power() - target.get_resistance() * target.get_level()) * damage_multiplier
        hero.update_mana(-self.get_mana_cost())
        if damage <= 0:
            damage = 0
            return
        print("{} casted a {} magic and deals {} points of {} damage to {}".format(
            hero.get_name(),
            self.get_type(),
            damage,
            self.get_attack_type(),
            target.get_name()
            ))
        print("This spell consume {} mana".format(self.get_mana_cost()))
        print(hero.infoMp)
        target.attacked(hero, damage)

class Knight(Role):
    def __init__(self, aura) -> None:
        self.__role = "warrior"
        self.__aura = aura
        self.__attack_type = "physical"
        self.__attack_growth = 9
        self.__health_growth = 150
        self.__mana_growth = 75
        self.__defense_growth = 4
        self.__resistance_growth = 3
        self.__health_cost = 30
        self.__mana_cost = 15
        self.__health_regen = 3
        self.__mana_regen = 1

    def get_role(self):
        return self.__role

    def get_type(self):
        return self.__aura

    def get_attack_type(self):
        return self.__attack_type
    
    def get_attack_growth(self):
        return self.__attack_growth
    
    def get_health_growth(self):
        return self.__health_growth
    
    def get_mana_growth(self):
        return self.__mana_growth
    
    def get_defense_growth(self):
        return self.__defense_growth
    
    def get_resistance_growth(self):
        return self.__resistance_growth
    
    def get_mana_cost(self):
        return self.__mana_cost
    
    def get_health_cost(self):
        return self.__health_cost
    
    def get_health_regen(self):
        return self.__health_regen
    
    def get_mana_regen(self):
        return self.__mana_regen
    
    def attack(self, hero: Character, target: Character):
        damage_multiplier = 0.5 + hero.get_level() / target.get_level()
        damage = hero.get_weapon().getWeaponPower() * 0.5 + (hero.get_attack_power() - target.get_defense() * target.get_level()) * damage_multiplier
        damage += self.get_health_cost() * damage_multiplier
        hero.update_mana(-self.get_mana_cost())
        hero.update_health(-self.get_health_cost())
        if damage <= 0:
            damage = 0
            return
        print("{} swing his weapon with {} aura and deals {} points of {} damage to {}".format(
            hero.get_name(),
            self.get_type(),
            damage,
            self.get_attack_type(),
            target.get_name()
            ))
        print("This attack consume {} mana and {} health".format(self.get_mana_cost(), self.get_health_cost()))
        print(hero.infoMp)
        print(hero.infoHp)
        target.attacked(hero, damage)