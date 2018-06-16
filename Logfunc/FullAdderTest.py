from FullAdder import FullAdder
import unittest

class FullAdderTest(unittest.TestCase):
    def testcase_02(self):
        a = FullAdder()
        testdatas = [
            [False, False, False, False, False],
            [False, False, True, True, False],
            [False, True, False, True, False],
            [False, True, True, False, True],
            [True, False, False, True, False],
            [True, False, True, False, True],
            [True, True, False, False, True],
            [True, True, True, True, True]
        ]
        for testdata in testdatas:
            a.set_input(testdata[0], testdata[1], testdata[2])
            a.execute()
            self.assertEqual(testdata[3], a.get_output_sum(), "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[4], a.get_output_carry(), "Class FullAdder Testcase 2 failed: " + testdata.__str__())


if __name__ == "__main__":
    unittest.main()