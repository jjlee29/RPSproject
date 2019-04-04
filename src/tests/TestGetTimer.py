import unittest
from Backend import rps


class TestTimer(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.timer(["Edward", "Joyce", "Cheng", "Jason", "Connie", "Wilfred", "Jack", "Jill"]), "Start Game!")


if __name__ == '__main__':
    unittest.main()
