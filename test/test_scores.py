import unittest
from unittest.mock import patch

from dictionary_update_assignment.scores import get_test_score, average_scores


class TestClass(unittest.TestCase):
    @patch('dictionary_update_assignment.scores.input')  # Decided to go with mock testing
    def test_scores(self, mock_input):
        mock_input.side_effect = [2, 85, 90]  # The first value is the number of tests taken, the second and third value represent the score received.
        expected = dict(test1=85, test2=90)
        actual = get_test_score()

        self.assertEqual(actual, expected)

# The rest of the tests are for exception handling (except for the final)

    @patch('dictionary_update_assignment.scores.input')
    def test_get_test_score_raises_error_when_it_cannot_validate(self, mock_input):
        mock_input.side_effect = ['Hello']
        with self.assertRaises(ValueError):
            get_test_score()

    @patch('dictionary_update_assignment.scores.input')
    def test_get_test_score_raise_error_when_value_is_negative(self, mock_input):
        mock_input.side_effect = [-1]
        with self.assertRaises(ValueError):
            get_test_score()

    @patch('dictionary_update_assignment.scores.input')
    def test_get_test_score_when_invalid_raise_error(self, mock_input):
        mock_input.side_effect = [1, -15]
        with self.assertRaises(ValueError):
            get_test_score()

    @patch('dictionary_update_assignment.scores.input')
    def test_get_test_score_when_given_string_raise_error(self, mock_input):
        mock_input.side_effect = [1, 'Hello']
        with self.assertRaises(ValueError):
            get_test_score()

    def test_average_scores(self):
        scores = dict(test1=85, test2=90)
        actual = average_scores(scores=scores)

        self.assertEqual(actual, 87.5)


if __name__ == '__main__':
    unittest.main()
