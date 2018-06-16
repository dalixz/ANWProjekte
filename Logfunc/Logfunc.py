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
        # _ = Protected
        self._Inputs = []
        self._Name = ""
        self._Outputs = []
        #Initialisierung der Ausgangswerte
        self.execute()

    def show(self):
        print(str(self))

    def set_inputs(self, Inputs):
        self._Inputs = Inputs

    def get_input_at(self, index):
        return self._Inputs[index]

    def get_output_at(self, index):
        return self._Outputs[index]

    def get_outputs(self):
        return self._Outputs

    def get_name(self):
        return self._Name

    @abstractmethod
    def execute(self):
        pass #nur für intellisense

# Kindklasse für AND-Gate
class AndGate(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "AndGate"

    def execute(self):
        self._Outputs = [True]
        for x in self._Inputs:
            if x is False:
                self._Outputs[0] = False
                break

# Kindklasse für OR-Gate
class OrGate(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "OrGate"

    def execute(self):
        self._Outputs = [False]
        for x in self._Inputs:
            if x is True:
                self._Outputs[0] = True
                break

# Kindklasse für XOR-Gate
class XOrGate(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "XOrGate"

    def execute(self):
        allTrue = True
        allFalse = True
        for x in self._Inputs:
            if not x:
                allTrue = False
            if x:
                allFalse = False

        result = (not allTrue) and (not allFalse)
        self._Outputs = [result]

# Kindklasse für NAND-Gate
class NAndGate(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "NAndGate"

    def execute(self):
        self._Outputs = [False]
        for x in self._Inputs:
            if x is False:
                self._Outputs[0] = True
                break