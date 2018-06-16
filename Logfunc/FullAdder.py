from Logfunc import LogFunc
from Logfunc import OrGate
from HalfAdder import HalfAdder

class FullAdder(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "HalfAdder"

    def set_input(self, a, b, carry):
        self._Inputs = [a, b, carry]

    def get_output_sum(self):
        return self.get_output_at(0)

    def get_output_carry(self):
        return self.get_output_at(1)

    def execute(self):

        #Workaround: Die LogFunc-Klasse ruft bei __init__ die execute-Methode auf um manche Logikgatter zu initialisieren. Zu dem Zeipunkt sind noch keine Input-Werte gesetzt
        if len(self._Inputs) == 0:
            return

        input_a = self.get_input_at(0)
        input_b = self.get_input_at(1)
        input_c = self.get_input_at(2)

        #Logikgatter erzeugen
        ha0 = HalfAdder()
        ha1 = HalfAdder()
        or0 = OrGate()

        #1. Halbaddierer aus a und b
        ha0.set_inputs([input_a, input_b])
        ha0.execute()

        #2. Halbaddierer aus 1. Halbaddierer Carry und c
        ha1.set_inputs([ha0.get_output_carry(), input_c])
        ha1.execute()

        or0.set_inputs([ha0.get_output_sum(), ha1.get_output_sum()])
        or0.execute()

        self._Outputs = [ha1.get_output_carry(), or0.get_output_at(0)]