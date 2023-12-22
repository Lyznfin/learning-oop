from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name:str, hp:float, mp:float, dp:float, rp:float, ap:float, role:classmethod) -> None:
        self.__name = name
        self.__max_health = hp
        self.__health = self.getMaxHealth()
        self.__max_mana = mp
        self.__mana = self.getMaxMana()
        self.__defense = dp
        self.__resistance = rp
        self.__attack_power = ap
        self.__shield = 0
        self.__exp = 0
        self.__level = 1
        self.__isAlive = True
        self.__role = role
        self.__exp_treshold = self.getLevel() * 2 * 50

    def getName(self):
        return self.__name
    
    def getMaxHealth(self):
        return self.__max_health

    def getHealth(self):
        return self.__health
    
    def setHealth(self, value):
        self.__health += value
    
    def getMana(self):
        return self.__mana
    
    def setMana(self, value):
        self.__mana += value
    
    def getMaxMana(self):
        return self.__max_mana
    
    def getDefense(self):
        return self.__defense
    
    def setDefense(self, value):
        self.__defense += value
    
    def getResistance(self):
        return self.__resistance
    
    def setResistance(self, value):
        self.__resistance += value

    def getAttackPower(self):
        return self.__attack_power
    
    def setAttackPower(self, value):
        self.__attack_power += value
    
    def getStatus(self):
        return self.__isAlive
    
    def getExp(self):
        return self.__exp
    
    def getExpTreshold(self):
        return self.__exp_treshold
    
    def setExpTreshold(self):
        self.__exp_treshold = self.getLevel() * 2 * 50
    
    def getLevel(self):
        return self.__level
    
    def getRole(self):
        return self.__role
    
    def setWeapon(self, weapon):
        self.__weapon = weapon

    def getWeapon(self):
        return self.__weapon

    def setSkill(self, skill):
        self.__skill = skill

    def getSkill(self):
        return self.__skill
    
    def getShield(self):
        return self.__shield
    
    def setShield(self, value):
        self.__shield = value

    def addShield(self, value):
        self.__shield += value

    def attack(self, target):
        if not self.getStatus():
            print("{} is dead, cannot attack".format(self.getName()))
            return
        if not target.getStatus():
            print("{} is dead, cannot be attacked".format(target.getName()))
            return
        elif self.getRole().getManaCost() > self.getMana():
            print(self.infoMp)
            print("{} mana is less than {}, cannot cast a basic spell".format(self.getName(), self.getRole().getManaCost()))
            return
        else:
            return self.getRole().attack(self, target)
        
    def useSkill(self, target):
        if not self.getStatus():
            print("{} is dead, cannot attack".format(self.getName()))
            return
        elif not target.getStatus():
            print("{} is dead, cannot be attacked".format(target.getName()))
            return
        if self.getSkill().getSkillCost() > self.getMana():
            print(self.infoMp)
            print("{} doesnt have enough mana to use skill: {}".format(
                self.getName(),
                self.getSkill().getName()
            ))
            return
        else:
            self.getSkill().useSkill(self, target)
        
    def useAbility(self, target):
        if not self.getStatus():
            print("{} is dead, cannot use ability".format(self.getName()))
            return
        elif not target.getStatus():
            print("{} is dead, cannot be attacked".format(target.getName()))
            return
        else:
            return self.getWeapon().useAbility(self, target)

    def reduceDamage(self, damage):
        if damage <= self.getShield() and self.getShield() != 0:
            print('{} points damage has completely been absorbed'.format(damage, self.getName()))
            self.addShield(-damage)
            damage = 0
            print('{} has {} points of shield left'.format(self.getName(), self.getShield()))
        elif damage > self.getShield() and self.getShield() != 0:
            absorbed = damage
            damage -= self.getShield() 
            absorbed -= damage
            print('{} points of damage has been absorbed'.format(absorbed))
            print('{} shields is now completely gone'.format(self.getName()))
            self.setShield(0)
        return damage

    def attacked(self, attacker, damage):
        if self.getShield() > 0:
            damage = self.reduceDamage(damage)
        self.setHealth(-round(damage))
        if damage <= 0:
            print('No ammount of damage is dealt to {}'.format(self.getName()))
            damage = 0
            return
        else:
            print("{} health has decreased by {} points".format(self.getName(), damage))
            if self.getHealth() <= 0:
                self.heroDied()
                expGain = (self.getExp() / 2) + 50
                attacker.setExp(expGain)
                return
            else:
                print(self.infoHp)

    def setExp(self, exp):
        self.__exp += exp
        if self.getExp() >= self.getExpTreshold():
            self.levelUp()

    def levelUp(self):
        if self.getLevel() % 5 == 0:
            print("{} has reached level {}, you can choose a skill based on you role of {} {}!".format(
                self.getName(),
                self.getLevel(),
                self.getRole().getType(),
                self.getRole().getRole()
            ))
            return
        else:
            self.setExp(-self.getExpTreshold())
            self.__attack_power += self.getRole().getAttackGrowth() * self.getLevel()
            self.__max_health += self.getRole().getHealthGrowth() * self.getLevel()
            self.__max_mana += self.getRole().getManaGrowth() * self.getLevel()
            self.setDefense(self.getRole().getDefenseGrowth() * self.getLevel())
            self.setResistance(self.getRole().getResistanceGrowth() * self.getLevel())
            self.__level += 1
            self.restoreStat()
            print("{} has leveled up".format(self.getName()))
            self.setExpTreshold()
            self.levelUp()
        return

    def restoreStat(self):
        self.__health = self.getMaxHealth()
        self.__mana = self.getMaxMana()

    def heroDied(self):
        self.__health = 0
        self.__mana = 0
        self.__isAlive = False
        self.__exp /= 2
        print("{} has died".format(self.getName()))

    def respawn(self):
        self.restoreStat()
        self.__isAlive = True

    def regen(self):
        health_regen = self.getRole().getHealthRegen() * self.getLevel()
        mana_regen = self.getRole().getManaRegen() * self.getLevel()

        if health_regen + self.getHealth() >= self.getMaxHealth():
            health_regen = self.getMaxHealth() - self.getHealth()
            self.setHealth(health_regen)
        else:
            self.setHealth(health_regen)
        
        if mana_regen + self.getMana() >= self.getMaxMana():
            mana_regen = self.getMaxMana() - self.getMana()
            self.setMana(mana_regen)
        else:
            self.setMana(mana_regen)

    @property
    def infoHp(self):
        if self.getStatus():
            return "{} has {}/{} health left".format(
                self.getName(), 
                self.getHealth(), 
                self.getMaxHealth(), 
                )
        else:
            return "{} is dead".format(
                self.getName()
            )
    
    @property
    def infoMp(self):
        if self.getMana() > 0:
            return "{} has {}/{} mana left".format(
                self.getName(), 
                self.getMana(), 
                self.getMaxMana()
                )
        else:
            return "{} has no mana left".format(
                self.getName()
            )
    
    @property
    def infoExp(self):
        return "{} needs {}/{} exp to level up".format(
            self.getName(), 
            self.getExp(),
            self.getExp() * (self.getLevel() * 2)
            )

class Role(ABC):
    @abstractmethod
    def attack(self, hero:Hero, target:Hero):
        pass

class Mage(Role):
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

    def getRole(self):
        return self.__role
    
    def getType(self):
        return self.__element

    def getAttackType(self):
        return self.__attack_type
    
    def getAttackGrowth(self):
        return self.__attack_growth
    
    def getHealthGrowth(self):
        return self.__health_growth
    
    def getManaGrowth(self):
        return self.__mana_growth
    
    def getDefenseGrowth(self):
        return self.__defense_growth
    
    def getResistanceGrowth(self):
        return self.__resistance_growth
    
    def getManaCost(self):
        return self.__mana_cost
    
    def getHealthRegen(self):
        return self.__health_regen
    
    def getManaRegen(self):
        return self.__mana_regen

    def attack(self, hero: Hero, target: Hero):
        damage_multiplier = 0.5 + hero.getLevel() / target.getLevel()
        damage = hero.getWeapon().getWeaponPower() * 0.5 + (hero.getAttackPower() - target.getResistance() * target.getLevel()) * damage_multiplier
        hero.setMana(-self.getManaCost())
        if damage <= 0:
            damage = 0
            return
        print("{} casted a {} magic and deals {} points of {} damage to {}".format(
            hero.getName(),
            self.getType(),
            damage,
            self.getAttackType(),
            target.getName()
            ))
        print("This spell consume {} mana".format(self.getManaCost()))
        print(hero.infoMp)
        target.attacked(hero, damage)

class Fighter(Role):
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

    def getRole(self):
        return self.__role

    def getType(self):
        return self.__aura

    def getAttackType(self):
        return self.__attack_type
    
    def getAttackGrowth(self):
        return self.__attack_growth
    
    def getHealthGrowth(self):
        return self.__health_growth
    
    def getManaGrowth(self):
        return self.__mana_growth
    
    def getDefenseGrowth(self):
        return self.__defense_growth
    
    def getResistanceGrowth(self):
        return self.__resistance_growth
    
    def getManaCost(self):
        return self.__mana_cost
    
    def getHealthCost(self):
        return self.__health_cost
    
    def getHealthRegen(self):
        return self.__health_regen
    
    def getManaRegen(self):
        return self.__mana_regen
    
    def attack(self, hero: Hero, target: Hero):
        damage_multiplier = 0.5 + hero.getLevel() / target.getLevel()
        damage = hero.getWeapon().getWeaponPower() * 0.5 + (hero.getAttackPower() - target.getDefense() * target.getLevel()) * damage_multiplier
        damage += self.getHealthCost() * damage_multiplier
        hero.setMana(-self.getManaCost())
        hero.setHealth(-self.getHealthCost())
        if damage <= 0:
            damage = 0
            return
        print("{} swing his weapon with {} aura and deals {} points of {} damage to {}".format(
            hero.getName(),
            self.getType(),
            damage,
            self.getAttackType(),
            target.getName()
            ))
        print("This attack consume {} mana and {} health".format(self.getManaCost(), self.getHealthCost()))
        print(hero.infoMp)
        print(hero.infoHp)
        target.attacked(hero, damage)