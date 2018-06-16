import Logfunc

test_and_gate = Logfunc.XOrGate()

test_and_gate.set_inputs([False, True])

test_and_gate.execute()
#test_and_gate.show()

print(test_and_gate.get_output_at(0))