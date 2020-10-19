import unittest
import datetime
from datetime_assignment.half_birthday import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.date(2020, 7, 15)
        expected_half_birthday = datetime.date(2021, 1, 13)

        actual = half_birthday(birthday)

        self.assertEqual(actual, expected_half_birthday)


if __name__ == '__main__':
    unittest.main()
