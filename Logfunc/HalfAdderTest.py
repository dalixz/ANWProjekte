from HalfAdder import HalfAdder
import unittest

class HalfAdderTest(unittest.TestCase):
    def assert_test_case(self, i1, i2, carry, sum):
        t = HalfAdder()
        t.set_inputs([i1, i2])
        t.execute()
        self.assertEqual(t.get_output_sum(), carry)
        self.assertEqual(t.get_output_carry(), sum)

    def testcase_01(self):
        self.assert_test_case(False, False, False, False)

    def testcase_02(self):
        self.assert_test_case(False, True, False, True)

    def testcase_03(self):
        self.assert_test_case(True, False, False, True)

    def testcase_04(self):
        self.assert_test_case(True, True, True, False)

if __name__ == "__main__":
    unittest.main()