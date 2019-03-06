import unittest
from Backend import rps


class TestGetWinner(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.winner(["Drake"]), "Drake is the winner!")
        self.assertEqual(rps.winner(["Jack", "Jill"]), "2 players remaining.")
        self.assertEqual(rps.winner(["Max"]), "Max is the winner!")
        self.assertEqual(rps.winner(["Jason", "Brandon", "Justin", "Jackson"]), "4 players remaining.")


if __name__ == '__main__':
    unittest.main()
