import Logfunc

test_and_gate = Logfunc.AndGate()

test_and_gate.__Input0 = True
test_and_gate.__Input1 = True

test_and_gate.execute()
#test_and_gate.show()

print(test_and_gate)