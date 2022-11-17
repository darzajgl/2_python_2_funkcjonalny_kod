import unittest


class TestCalculator(unittest.TestCase):
    TEST_CASES = [
        ((1, "+", 2, "="), 3),
        ((100, "-", 1, "-", 1, "-", 3, "="), 95),
        ((1, "+", 1, "-", 1, "+", 1, "-", 1, "+", 1, "-", 1, "="), 1),
    ]

    def test_multiple_cases(self):
        for call_arguments, expected_result in self.TEST_CASES:
            with self.subTest(call_arguments=call_arguments):
                self._single_test(call_arguments, expected_result)

    def _single_test(self, call_arguments, expected_result):
        from task8 import calculator

        returned_value = calculator
        for arg in call_arguments:
            returned_value = returned_value(arg)

        self.assertEqual(returned_value, expected_result)

    def test_no_globals_in_module(self):
        import task8

        allowed_globals = (
            "__builtins__",
            "__cached__",
            "__doc__",
            "__file__",
            "__loader__",
            "__name__",
            "__package__",
            "__spec__",
            "calculator",
        )

        for global_var in dir(task8):
            self.assertIn(global_var, allowed_globals)

    def test_no_globals_hacking(self):
        import task8
        import inspect

        globals_forbidden_in_code = (
            "__builtins__",
            "__cached__",
            "__doc__",
            "__file__",
            "__loader__",
            "__name__",
            "__package__",
            "__spec__",
        )

        module_source_code = inspect.getsource(task8)
        for forbidden_global in globals_forbidden_in_code:
            self.assertNotIn(forbidden_global, module_source_code)
