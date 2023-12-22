class Skill():
    def __init__(self, name:str, power:float, cost:float, type:str) -> None:
        self.__skill_name = name
        self.__skill_power = power
        self.__skill_cost = cost
        self.__skill_type = type
        self.__skill_exp = 0
        self.__skill_level = 1

    def getSkillName(self):
        return self.__skill_name
    
    def getSkillPower(self):
        return self.__skill_power
    
    def getSkillCost(self):
        return self.__skill_cost
    
    def getSkillType(self):
        return self.__skill_type
    
    def getSkillProficiency(self):
        return self.__skill_exp
    
    def getSkillLevel(self):
        return self.__skill_level
    
    def gainSkillProficiency(self, value:float):
        self.__skill_exp += value
    
    def levelUpSkill(self):
        self.__skill_level += 1
        return
    
class Bloodbound(Skill):
    def __init__(self) -> None:
        super().__init__("Bloodbound Vengeance", 126, 75, "physical")
        self.__buff = 1.5
        self.__buff_growth = 1
        self.__power_growth = 0.2
    
    def getBuff(self):
        return self.__buff
    
    def getBuffGrowth(self):
        return self.__buff_growth
    
    def getPowerGrowth(self):
        return self.__power_growth
    
    def getBuffDefense(self):
        return self.__buffDefense
    
    def getBuffResistance(self):
        return self.__buffResistance
        
    def useSkill(self, hero:classmethod, target:classmethod):
        self.gainSkillProficiency(50 + 12 * target.getLevel())
        hero.setMana(-self.getSkillCost())
        multiplier = self.getSkillLevel() * self.getBuffGrowth() + self.getBuff()
        self.__buffDefense = multiplier * hero.getDefense() - hero.getDefense()
        self.__buffResistance = multiplier * hero.getResistance() - hero.getResistance()
        print("{} has used {}, defences and resistances has been increased by {} and {} points".format(
            hero.getName(),
            self.getSkillName(),
            self.getBuffDefense(),
            self.getBuffResistance()
        ))
        hero.setDefense(self.getBuffDefense())
        hero.setResistance(self.getBuffResistance())
        damage = self.getSkillPower() + (self.getSkillPower() * self.getSkillLevel())
        damage = damage + damage * self.getPowerGrowth()
        damage -= target.getDefense() * target.getLevel()
        print("{} has infused his spear with an intensified blood aura, deals {} {} damage to {}".format(
            hero.getName(),
            damage,
            self.getSkillType(),
            target.getName()
        ))
        print("{} consumed {} mana".format(self.getSkillName(), self.getSkillCost()))
        print(hero.infoMp)
        target.attacked(hero, damage)
    
    def buffEnded(self, hero:classmethod):
        print("{} duration has ended".format(self.getSkillName()))
        hero.setDefense(-self.getBuffDefense())
        hero.setResistance(-self.getBuffResistance())

class Tempest(Skill):
    def __init__(self) -> None:
        super().__init__("Tempest Razorslash", 62, 95, "magical")
        self.__power_growth = 0.2
        self.__consecutive_attack = 3
    
    def getPowerGrowth(self):
        return self.__power_growth
    
    def getConsecutiveAttack(self):
        return self.__consecutive_attack
    
    def useSkill(self, hero:classmethod, target:classmethod):
        self.gainSkillProficiency(50 + 12 * target.getLevel())
        hero.setMana(-self.getSkillCost())
        damage = self.getSkillPower() + (self.getSkillPower() * self.getSkillLevel() * self.getPowerGrowth())
        damage -= target.getResistance() * target.getLevel()
        print("{} unleashed {}".format(
                hero.getName(),
                self.getSkillName()
        ))
        for _ in range(self.getConsecutiveAttack()):
            print("The bursts of wind deals {} {} damage to {}".format(
                round(damage, 1),
                self.getSkillType(),
                target.getName()
            ))
        print("{} consumed {} mana".format(self.getSkillName(), self.getSkillCost()))
        print(hero.infoMp)
        target.attacked(hero, round(damage * self.getConsecutiveAttack(), 1))