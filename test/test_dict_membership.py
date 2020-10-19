import unittest
from more_fun_with_collections.dict_membership import in_dict


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        values = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        expected = True

        actual = in_dict(values, 'A')
        self.assertEqual(actual, expected)

    def test_in_dict_false(self):
        values = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        expected = False

        actual = in_dict(values, 'G')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
