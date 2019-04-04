import unittest
from Backend import rps


class TestGetWinner(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.compChoice("rock"), "Computer chooses rock.")
        self.assertEqual(rps.compChoice("paper"), "Computer chooses paper.")
        self.assertEqual(rps.compChoice("scissors"), "Computer chooses scissors.")


if __name__ == '__main__':
    unittest.main()