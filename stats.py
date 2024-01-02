from abc import ABC, abstractmethod
from enum import Enum

#might be ridiculous, but belive me, this spageth classes is intentional
#well, as one might say, its for the purpose of research (i actually have no idea why im doing this)

class Base_Stats(Enum):
    HP = 400
    MP = 150
    SP = 120
    DEF = 15
    RES = 10
    CRIT = 0.15
    ASPD = 1

class Attribute(ABC):
    @classmethod
    @abstractmethod
    def get_ammount(cls) -> int:
        pass

    @abstractmethod
    def get_attribute(self) -> float:
        pass

class STR(Attribute):
    __ammount = 5
    def __init__(self, val) -> None:
        STR.__ammount += val

    @classmethod
    def get_ammount(cls) -> int:
        return cls.__ammount
    
    def get_attribute(self) -> float:
        pass

class DEX(Attribute):
    __ammount = 5
    def __init__(self, val) -> None:
        DEX.__ammount += val

    @classmethod
    def get_ammount(cls):
        return cls.__ammount
    
    def get_attribute(self) -> float:
        pass
    
class CON(Attribute):
    __ammount = 5
    def __init__(self, val) -> None:
        CON.__ammount += val

    @classmethod
    def get_ammount(cls):
        return cls.__ammount
    
    def get_attribute(self) -> float:
        pass
    
class INT(Attribute):
    __ammount = 5
    def __init__(self, val) -> None:
        INT.__ammount += val

    @classmethod
    def get_ammount(cls):
        return cls.__ammount
    
    def get_attribute(self) -> float:
        pass
    
class WIS(Attribute):
    __ammount = 5
    def __init__(self, val) -> None:
        WIS.__ammount += val

    @classmethod
    def get_ammount(cls):
        return cls.__ammount
    
    def get_attribute(self) -> float:
        pass

class Stats():
    def __init__(self, str, dex, con, int, wis) -> None:
        self.__STR = str
        self.__DEX = dex
        self.__CON = con
        self.__INT = int
        self.__WIS = wis

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
        pass

    def set_mana(self):
        pass

    def set_stamina(self):
        pass

    def set_crit(self):
        pass

    def set_attack_speed(self):
        pass

    def set_defense(self):
        pass
    
    def set_resistance(self):
        pass

    def set_weapon_attack(self):
        pass

    def print_stats(self):
        print('STR: {} \nDEX: {} \nCON: {} \nINT: {} \nWIS: {}'.format(
            self.get_STR().get_ammount(),
            self.get_DEX().get_ammount(),
            self.get_CON().get_ammount(),
            self.get_INT().get_ammount(),
            self.get_WIS().get_ammount()
        ))
    

obj = Stats(STR(3), DEX(4), CON(12), INT(21), WIS(12))

obj.print_stats()