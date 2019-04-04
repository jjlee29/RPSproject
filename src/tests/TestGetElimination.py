import unittest
from Backend import rps


class TestGetWinner(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.elimination("Phil", ["Phil", "Tracer", "Genji"]), ["Tracer", "Genji"])
        self.assertEqual(rps.elimination("Sombra", ["Arthur", "Eren", "Armin"]), ["Arthur", "Eren", "Armin"])
        self.assertEqual(rps.elimination("Gon", ["Killua", "Gon", "Gin", "Creed"]), ["Killua", "Gin", "Creed"])
        self.assertEqual(rps.elimination("Jacks", ["Kings", "Warp", "Wraith", "Joker", "Naruto"]), ["Kings", "Warp", "Wraith", "Joker", "Naruto"])


if __name__ == '__main__':
    unittest.main()