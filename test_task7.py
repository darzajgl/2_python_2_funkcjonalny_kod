import unittest
import secrets
from random import shuffle

CALL_TOKENS = [secrets.token_hex(16) for _ in range(100)]
CALLS_ORDER = []


def token_user_factory(token):
    def inner():
        CALLS_ORDER.append(token)

    return inner


FUNCTIONS = [token_user_factory(token) for token in CALL_TOKENS]


class TestMemorizerCaller(unittest.TestCase):
    def test_memorize_call(self):
        from task7 import memorizer, caller

        memorizer(FUNCTIONS)
        self.assertEqual([], CALLS_ORDER)

        shuffle(FUNCTIONS)
        caller(FUNCTIONS)

        self.assertEqual(CALL_TOKENS, CALLS_ORDER)

    def test_no_globals_in_module(self):
        import task7

        allowed_globals = (
            "__builtins__",
            "__cached__",
            "__doc__",
            "__file__",
            "__loader__",
            "__name__",
            "__package__",
            "__spec__",
            "caller",
            "memorizer",
        )

        for global_var in dir(task7):
            self.assertIn(global_var, allowed_globals)

    def test_no_globals_hacking(self):
        import task7
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

        module_source_code = inspect.getsource(task7)
        for forbidden_global in globals_forbidden_in_code:
            self.assertNotIn(forbidden_global, module_source_code)
