import unittest


class TestMultiCalculator(unittest.TestCase):

    TEST_CASES = [
        ((4, 4, 4), None, 12),
        ((1, 1, 1), "+", 3),
        ((10, 1, 1, 1, 1, 1, 1), "-", 4),
        ((2, 3, 4), "*", 24),
        (tuple(), "**", 0),
        ((235, 2345, 623, 123), "|", 3071),
        ((663,), "&", 663),
    ]

    def test_multiple_cases(self):
        for args, operation, expected_result in self.TEST_CASES:
            with self.subTest(args=args, operation=operation):
                self._single_test(args, operation, expected_result)

    def _single_test(self, args, operation, expected_result):
        from task2 import multi_calculator

        if operation:
            result = multi_calculator(*args, operation=operation)
        else:
            result = multi_calculator(*args)

        self.assertEqual(result, expected_result)
