from FullAdder import FullAdder
from Logfunc import LogFunc

class EightBitAdder(LogFunc):
    def __init__(self):
        LogFunc.__init__(self)
        self._Name = "EightBitAdder"

    def set_input_binary(self, binary_a, binary_b, carry = False):
        #length check
        if len(binary_a) is not 8:
            raise ValueError("Invalid Bit length! binary_a")
        if len(binary_b) is not 8:
            raise ValueError("Invalid Bit length! binary_a")

        #type check
        if type(carry) is not bool:
            raise ValueError("Invalid carry!")
        if not all(isinstance(n, bool) for n in binary_a):
            raise ValueError("Invalid DataType! binary_a")
        if not all(isinstance(n, bool) for n in binary_b):
            raise ValueError("Invalid DataType! binary_b")

        self.set_inputs([carry] + binary_a + binary_b)

    def get_output_binary(self):
        if len(self._Outputs) is 0:
            raise ValueError("Please use execute()")
        return self._Outputs[1:9]

    def get_output_carry(self):
        if len(self._Outputs) is 0:
            raise ValueError("Please use execute()")
        return self._Outputs[0]

    def execute(self):
        #Workaround: Die LogFunc-Klasse ruft bei __init__ die execute-Methode auf um manche Logikgatter zu initialisieren. Zu dem Zeipunkt sind noch keine Input-Werte gesetzt
        if len(self._Inputs) == 0:
            return

        if len(self._Inputs) is not 17:
            raise ValueError("Invalid Input Values")

        #Werte aus Inputs extrahieren
        last_carry = self.get_input_at(0)
        inputs_a = self._Inputs[1:9]
        inputs_b = self._Inputs[9:18]

        half_adder_sums = []

        #Rückwärts durch Inputs iterieren
        for x in reversed(range(0, 8)):
            fa = FullAdder()
            fa.set_input(inputs_a[x], inputs_b[x], last_carry)
            fa.execute()
            #Übertrag für nächsten FullAdder speichern
            last_carry = fa.get_output_carry()
            #Summe am Anfang (index 0) der Ergebnisliste speichern
            half_adder_sums.insert(0, fa.get_output_sum())


        self._Outputs = [last_carry] + half_adder_sums




