import unittest
from selection_dictionary_assignment.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_switch_average_given_A(self):
        average = 12.5
        actual = switch_average('A')

        self.assertEqual(actual, average)

    def test_switch_average_given_B(self):
        average = 30
        actual = switch_average('B')

        self.assertEqual(actual, average)

    def test_switch_average_given_C(self):
        average = 2
        actual = switch_average('C')

        self.assertEqual(actual, average)

    def test_switch_average_given_D(self):
        average = 5
        actual = switch_average('D')

        self.assertEqual(actual, average)

    def test_switch_average_given_invalid_key(self):
        with self.assertRaises(ValueError):

            switch_average('K')


if __name__ == '__main__':
    unittest.main()
