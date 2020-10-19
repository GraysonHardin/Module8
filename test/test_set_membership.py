import unittest
from more_fun_with_collections.set_membership import in_set


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        values = {1, 2, 3, 4, 5}
        expected = True

        actual = in_set(values, 5)
        self.assertEqual(actual, expected)

    def test_in_set_false(self):
        values = {1, 2, 3, 4, 5}
        expected = False

        actual = in_set(values, 6)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
