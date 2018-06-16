from Logfunc import LogFunc
from Logfunc import AndGate
from Logfunc import XOrGate

class HalfAdder(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "HalfAdder"

    def execute(self):

        #Workaround: Die LogFunc-Klasse ruft bei __init__ die execute-Methode auf um manche Logikgatter zu initialisieren. Zu dem Zeipunkt sind noch keine Input-Werte gesetzt
        if len(self._Inputs) == 0:
            return

        sum = XOrGate()
        sum.set_inputs([self.get_input_at(0), self.get_input_at(1)])
        sum.execute()

        carry = AndGate()
        carry.set_inputs([self.get_input_at(0), self.get_input_at(1)])
        carry.execute()

        sum_result = sum.get_output_at(0)
        carry_result = carry.get_output_at(0)

        self._Outputs = [carry_result, sum_result]

    def get_output_sum(self):
        return self.get_output_at(0)

    def get_output_carry(self):
        return self.get_output_at(1)