import unittest


class TestMultiAdders(unittest.TestCase):

    TEST_CASES = [(5, [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]), (3, [10, 3, 1], [10, 4, 3])]

    def test_multiple_cases(self):
        for n, inputs, outputs in self.TEST_CASES:
            with self.subTest(n=n, inputs=inputs):
                self._single_test(n, inputs, outputs)

    def _single_test(self, n, inputs, outputs):
        from task5 import multi_adders

        functions = multi_adders(n)
        for function, input, output in zip(functions, inputs, outputs):
            self.assertEqual(output, function(input))
