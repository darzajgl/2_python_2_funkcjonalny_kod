import unittest


class TestSimpleFunctionalCalc(unittest.TestCase):

    TEST_CASES = [
        (1, "+", 1, 2),
        (1, "-", 1, 0),
        (10, "+", 123, 133),
        (0, "-", 5, -5),
    ]

    def test_multiple_cases(self):
        from task6 import simple_functional_calc

        for test_case in self.TEST_CASES:
            arg1, op, arg2, expected_result = test_case
            with self.subTest(arg1=arg1, op=op, arg2=arg2):
                result = simple_functional_calc(arg1)(op)(arg2)
                self.assertEqual(result, expected_result)
