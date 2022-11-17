import unittest


class TestSimpleAdder(unittest.TestCase):
    TEST_CASES = [
        ((0, 0), 0),
        ((1, 4), 5),
        ((10, -21), -11),
        ((-100, 100), 0),
    ]

    def test_multiple_cases(self):
        from task1 import simple_adder

        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = simple_adder(*input)
                self.assertEqual(result, expected_result)


class TestSimpleSubtractor(unittest.TestCase):
    TEST_CASES = [
        ({"x": 10, "y": 5}, 5),
        ({"x": 1, "y": 4}, -3),
        ({"x": 10, "y": -21}, 31),
        ({"x": -100, "y": 100}, -200),
    ]

    def test_multiple_cases(self):
        from task1 import simple_subtractor

        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                result = simple_subtractor(**input)
                self.assertEqual(result, expected_result)


class TestSimpleCalculator(unittest.TestCase):

    TEST_CASES = [
        ((5, 5, None), 10),
        ((10, 4, "-"), 6),
        ((11, 12, "*"), 132),
        ((6, 2, "**"), 36),
        ((324, 523, "|"), 847),
        ((1111, 2341, "&"), 5),
    ]

    def test_multiple_cases(self):
        from task1 import simple_calculator

        for input, expected_result in self.TEST_CASES:
            with self.subTest(input=input):
                x, y, op = input
                if op:
                    result = simple_calculator(x, y, operation=op)
                else:
                    result = simple_calculator(x, y)
                self.assertEqual(result, expected_result)
