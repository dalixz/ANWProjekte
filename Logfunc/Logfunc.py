#Libs
from abc import ABC, abstractmethod

# Verwaltungsinfos
__version__ = "1.0"
__author__ = "DLI"

# Elternklasse
class LogFunc(ABC):
    def __init__(self):
        # Attribute definieren
        # __ = Private
        self.__Input0 = False
        self.__Input1 = False
        self.__Name = ""
        # _ Protected
        self._Output = False
        #Initialisierung der Ausgangswerte
        self.execute()

    def show(self):
        print(str(self))

    def set_input(self, Input0, Input1, Name):
        self.__Input0 = Input0
        self.__Input1 = Input1
        self.__Name = Name

    def get_input0(self):
        return self.__Input0

    def get_input1(self):
        return self.__Input1

    def get_output(self):
        return self._Output

    def get_name(self):
        return self.__Name

    def __str__(self):
        str = "Ergibt Falsch"
        if True == self._Output:
            str = "Ergibt Richtig"

        return str

    @abstractmethod
    def execute(self):
        pass #nur für intellisense

# Kindklasse für AND-Gate
class AndGate(LogFunc):
    def execute(self):
        self._Output = False
        if self.get_input1() == self.get_input0():
            if True == self.get_input0():
                self._Output = True

# Kindklasse für OR-Gate
class OrGate(LogFunc):
    def execute(self):
        self._Output = False
        if self.get_input0() == True:
            self._Output = True
        if self.get_input1() == True:
            self._Output = True

# Kindklasse für XOR-Gate
class XOrGate(LogFunc):
    def execute(self):
        self._Output = self.get_input0() != self.get_input1()

# Kindklasse für NAND-Gate
class NAndGate(LogFunc):
    def execute(self):
        self._Output = True
        if self.get_input1() == self.get_input0():
            if True == self.get_input0():
                self._Output = False