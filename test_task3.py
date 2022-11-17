import unittest


class TestListUpdater(unittest.TestCase):

    TEST_CASES = [
        ((1, 2, 3), None, [1, 2, 3]),
        (("a", "b", "c"), [1, 2], [1, 2, "a", "b", "c"]),
        (("test", "test", "test"), None, ["test", "test", "test"]),
        ((), None, []),
        ((), [1, 2, 3, 11], [1, 2, 3, 11]),
    ]

    def test_multiple_cases(self):
        for args, collection, expected_result in self.TEST_CASES:
            with self.subTest(args=args, collection=collection):
                self._single_test(args, collection, expected_result)

    def _single_test(self, args, collection, expected_result):
        from task3 import list_updater

        if collection:
            result = list_updater(*args, collection=collection)
        else:
            result = list_updater(*args)

        self.assertEqual(result, expected_result)
