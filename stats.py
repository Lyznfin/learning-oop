from abc import ABC, abstractmethod
from enum import Enum
from weapon import Weapon_Types

#might be ridiculous, but belive me, this spageth classes is intentional
#well, as one might say, its for the purpose of research (i actually have no idea why im doing this)

class Base_Stats(Enum):
    HP = 400
    MP = 150
    SP = 120
    CRIT = 0.05
    CRITDMG = 0.5
    ASPD = 1
    DEF = 15
    RES = 10

class Attribute(ABC):
    @abstractmethod
    def get_ammount(self) -> int:
        pass

    @abstractmethod
    def set_ammount(self, val) -> int:
        pass

    @abstractmethod
    def update_ammount(self, val) -> int:
        pass

class STR(Attribute):
    def __init__(self, val:int=0) -> None:
        self.__ammount = 5
        self.update_ammount(val)

    def get_ammount(self) -> int:
        return self.__ammount

    def set_ammount(self, val) -> int:
        self.__ammount = val
    
    def update_ammount(self, val) -> int:
        self.__ammount += val

class DEX(Attribute):
    def __init__(self, val:int=0) -> None:
        self.__ammount = 5
        self.update_ammount(val)

    def get_ammount(self) -> int:
        return self.__ammount

    def set_ammount(self, val) -> int:
        self.__ammount = val
    
    def update_ammount(self, val) -> int:
        self.__ammount += val
    
class CON(Attribute):
    def __init__(self, val:int=0) -> None:
        self.__ammount = 5
        self.update_ammount(val)

    def get_ammount(self) -> int:
        return self.__ammount

    def set_ammount(self, val) -> int:
        self.__ammount = val
    
    def update_ammount(self, val) -> int:
        self.__ammount += val
    
class INT(Attribute):
    def __init__(self, val:int=0) -> None:
        self.__ammount = 5
        self.update_ammount(val)

    def get_ammount(self) -> int:
        return self.__ammount

    def set_ammount(self, val) -> int:
        self.__ammount = val
    
    def update_ammount(self, val) -> int:
        self.__ammount += val
    
class WIS(Attribute):
    def __init__(self, val:int=0) -> None:
        self.__ammount = 5
        self.update_ammount(val)

    def get_ammount(self) -> int:
        return self.__ammount

    def set_ammount(self, val) -> int:
        self.__ammount = val
    
    def update_ammount(self, val) -> int:
        self.__ammount += val

class StatsCalculator:
    @staticmethod
    def calculate_hp(con_value:int):
        return round(Base_Stats.HP.value + (Base_Stats.HP.value * (0.35 * con_value)) * 0.2)
    
    @staticmethod
    def calculate_mp(wis_value:int):
        return round(Base_Stats.MP.value + (Base_Stats.MP.value * (0.2 * wis_value)) * 0.25)
    
    @staticmethod
    def calculate_sp(con_value:int):
        return round(Base_Stats.SP.value + (Base_Stats.SP.value * (0.2 * con_value)) * 0.22)
    
    @staticmethod
    def calculate_crit(dex_value:int):
        return round(Base_Stats.CRIT.value + (0.05 * dex_value) * 0.05, 3)
    
    @staticmethod
    def calculate_critdmg(dex_value:int):
        return round(Base_Stats.CRITDMG.value + (0.25 * dex_value) * 0.1, 3)
    
    @staticmethod
    def calculate_aspd(dex_value:int):
        return round(Base_Stats.ASPD.value + (Base_Stats.ASPD.value * (0.05 * dex_value)) * 0.2, 3)

    @staticmethod
    def calculate_defense(str_value:int, con_value:int):
        return round(Base_Stats.DEF.value + ((0.75 * str_value) + (1.5 * con_value)) * 0.7)
    
    @staticmethod
    def calculate_resistance(int_value:int, wis_value:int):
        return round(Base_Stats.RES.value + ((0.75 * int_value) + (1.5 * wis_value)) * 0.7)

class Stats:
    def __init__(self, str:classmethod, dex:classmethod, con:classmethod, int:classmethod, wis:classmethod) -> None:
        self.check_input(str, dex, con, int, wis)

        self.__STR = str
        self.__DEX = dex
        self.__CON = con
        self.__INT = int
        self.__WIS = wis

        self.initialize_stats()

    @staticmethod
    def check_input(str, dex, con, int, wis):
        assert str.get_ammount() >= 5, f"input stat can not be below zero!"
        assert dex.get_ammount() >= 5, f"input stat can not be below zero!"
        assert con.get_ammount() >= 5, f"input stat can not be below zero!"
        assert int.get_ammount() >= 5, f"input stat can not be below zero!"
        assert wis.get_ammount() >= 5, f"input stat can not be below zero!"        

    def initialize_stats(self):
        self.set_health()
        self.set_mana()
        self.set_stamina()
        self.set_crit()
        self.set_critdmg()
        self.set_attack_speed()
        self.set_defense()
        self.set_resistance()

    def get_STR(self):
        return self.__STR

    def get_DEX(self):
        return self.__DEX

    def get_CON(self):
        return self.__CON

    def get_INT(self):
        return self.__INT

    def get_WIS(self):
        return self.__WIS

    def set_health(self):
        self.__health = StatsCalculator.calculate_hp(
            self.get_CON().get_ammount()
        )

    def set_mana(self):
        self.__mana = StatsCalculator.calculate_mp(
            self.get_WIS().get_ammount()
        )

    def set_stamina(self):
        self.__stamina = StatsCalculator.calculate_sp(
            self.get_CON().get_ammount()
        )

    def set_crit(self):
        self.__crit = StatsCalculator.calculate_crit(
            self.get_DEX().get_ammount()
        )

    def set_critdmg(self):
        self.__critdmg = StatsCalculator.calculate_critdmg(
            self.get_DEX().get_ammount()
        )

    def set_attack_speed(self):
        self.__aspd = StatsCalculator.calculate_aspd(
            self.get_DEX().get_ammount()
        )

    def set_defense(self):
        self.__defense = StatsCalculator.calculate_defense(
            self.get_STR().get_ammount(), self.get_CON().get_ammount()
        )
    
    def set_resistance(self):
        self.__resistance = StatsCalculator.calculate_resistance(
            self.get_INT().get_ammount(), self.get_WIS().get_ammount()
        )

    '''
    def set_weapon_attack(self):
        match Weapon_Types.value:
            case 'Sword':
                pass
            case 'Polearm':
                pass
            case 'Bow':
                pass
            case 'Wand':
                pass
            case 'Axe':
                pass
            case 'Firearm':
                pass
            case 'Gauntlet':
                pass
            case 'Orb':
                pass
            case 'Hammer':
                pass
            case 'Unique':
                pass '''

    def print_attribute(self):
        print('STR: {} \nDEX: {} \nCON: {} \nINT: {} \nWIS: {}'.format(
            self.get_STR().get_ammount(),
            self.get_DEX().get_ammount(),
            self.get_CON().get_ammount(),
            self.get_INT().get_ammount(),
            self.get_WIS().get_ammount()
        ))

    def print_stats(self):
        print('HP: {} \nMP: {} \nSP: {} \nCRIT: {} \nCRIT DMG: {} \nASPD: {} \nDEF: {} \nRES: {}'.format(
            self.__health,
            self.__mana,
            self.__stamina,
            self.__crit,
            self.__critdmg,
            self.__aspd,
            self.__defense,
            self.__resistance
        ))

#obj = Stats(STR(5), DEX(6), CON(12), INT(21), WIS(12))

#obj.print_attribute()
#obj.print_stats()