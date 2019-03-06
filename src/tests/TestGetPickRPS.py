import unittest
from Backend import rps


class TestGetPickRPS(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.pickRPS("Harry", "i[0]"), "Harry chooses rock.")
        self.assertEqual(rps.pickRPS("Michael", "i[1]"), "Michael chooses paper.")
        self.assertEqual(rps.pickRPS("Edward", "i[2]"), "Edward chooses scissor.")
        self.assertEqual(rps.pickRPS("Ricky", " "), "Did not choose in time.")


if __name__ == '__main__':
    unittest.main()