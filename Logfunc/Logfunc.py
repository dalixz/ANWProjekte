# Verwaltungsinfos
__version__ = "1.0"
__author__ = "DLI"

# Elternklasse
class LogFunc:
    def __init__(self):
        # _ = Protected
        # Attribute definieren
        self._Input0 = False
        self._Input1 = False
        self._Output = False
        self._Name = ""

    def show(self):
        print(str(self))

    def set_input(self, Input0, Input1, Name):
        self._Input0 = Input0
        self._Input1 = Input1
        self._Name = Name

    def get_input(self):
        return self._Output

    def get_name(self):
        return self._Name

    def __str__(self):
        str = "Ergibt Falsch"
        if True == self._Output:
            str = "Ergibt Richtig"

        return str

# Kindklasse für AND-Gate
class AndGate(LogFunc):
    def execute(self):
        self._Output = False
        if self._Input1 == self._Input0:
            if True == self._Input0:
                self._Output = True

# Kindklasse für OR-Gate
class OrGate(LogFunc):
    def execute(self):
        self._Output = False
        if self._Input0 == True:
            self._Output = True
        if self._Input1 == True:
            self._Output = True

# Kindklasse für XOR-Gate
class XOrGate(LogFunc):
    def execute(self):
        self._Output = self._Input0 != self._Input1