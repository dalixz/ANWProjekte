import unittest
from Logfunc import AndGate
from Logfunc import OrGate
from Logfunc import XOrGate

class AndGateTest(unittest.TestCase):
    def assert_test_case(self, in0, in1, out, test_id):
        a = AndGate()
        a.set_input(in0, in1, "TestAndGate")
        a.execute()
        if out:
            self.assertTrue(a.get_input(), "Class AndGate: " + test_id + " failed")
        else:
            self.assertFalse(a.get_input(), "Class AndGate: " + test_id + " failed")

    def testcase_01(self):
        self.assert_test_case(False, False, False, "Test 1")

    def testcase_02(self):
        self.assert_test_case(True, False, False, "Test 2")

    def testcase_03(self):
        self.assert_test_case(False, True, False, "Test 3")

    def testcase_04(self):
        self.assert_test_case(True, True, True, "Test 4")

class OrGateTest(unittest.TestCase):
    def assert_test_case(self, in0, in1, out, test_id):
        a = OrGate()
        a.set_input(in0, in1, "TestOrGate")
        a.execute()
        if out:
            self.assertTrue(a.get_input(), "Class OrGate: " + test_id + " failed")
        else:
            self.assertFalse(a.get_input(), "Class OrGate: " + test_id + " failed")

    def testcase_01(self):
        self.assert_test_case(False, False, False, "Test 1")

    def testcase_02(self):
        self.assert_test_case(True, False, True, "Test 2")

    def testcase_03(self):
        self.assert_test_case(False, True, True, "Test 3")

    def testcase_04(self):
        self.assert_test_case(True, True, True, "Test 4")

class XOrGateTest(unittest.TestCase):
    def assert_test_case(self, in0, in1, out, test_id):
        a = XOrGate()
        a.set_input(in0, in1, "TestXOrGate")
        a.execute()
        if out:
            self.assertTrue(a.get_input(), "Class XOrGate: " + test_id + " failed")
        else:
            self.assertFalse(a.get_input(), "Class XOrGate: " + test_id + " failed")

    def testcase_01(self):
        self.assert_test_case(False, False, False, "Test 1")

    def testcase_02(self):
        self.assert_test_case(True, False, True, "Test 2")

    def testcase_03(self):
        self.assert_test_case(False, True, True, "Test 3")

    def testcase_04(self):
        self.assert_test_case(True, True, False, "Test 4")


if __name__ == "__main__":
    unittest.main()                 # Führt automatisch alle Methoden aus, die mit "Testcase_" beginnen