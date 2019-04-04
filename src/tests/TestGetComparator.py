import unittest
from Backend import rps


class TestGetWinner(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.comparator("Apple", "rock", "paper"), "Paper covers rock. Computer wins.")
        self.assertEqual(rps.comparator("Grape", "rock", "scissors"), "Rock crushes scissors. Grape wins.")
        self.assertEqual(rps.comparator("Peach", "paper", "scissors"), "Scissors cuts paper. Computer wins.")
        self.assertEqual(rps.comparator("Strawberry", "paper", "rock"), "Paper covers rock. Strawberry wins.")
        self.assertEqual(rps.comparator("Mario", "scissors", "rock"), "Rock crushes scissors. Computer wins.")
        self.assertEqual(rps.comparator("Luigi", "scissors", "paper"), "Scissors cuts paper. Luigi wins.")
        self.assertEqual(rps.comparator("Luigi", "rock", "rock"), "Draw!")
        self.assertEqual(rps.comparator("Luigi", "paper", "paper"), "Draw!")
        self.assertEqual(rps.comparator("Luigi", "scissors", "scissors"), "Draw!")


if __name__ == '__main__':
    unittest.main()