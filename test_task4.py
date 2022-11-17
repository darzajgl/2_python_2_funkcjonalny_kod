import unittest


class TestAdder(unittest.TestCase):

    TEST_CASES = [
        (1, 1, 2),
        (-2, -2, -4),
        (0, 0, 0),
    ]

    def test_multiple_cases(self):
        from task4 import adder

        for arg1, arg2, expected_result in self.TEST_CASES:
            with self.subTest(arg1=arg1, arg2=arg2):
                result = adder(arg1)(arg2)
                self.assertEqual(result, expected_result)
