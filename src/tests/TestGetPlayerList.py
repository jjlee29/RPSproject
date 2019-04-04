import unittest
from Backend import rps


class TestTimer(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rps.playerList("Happy", []), ["Happy"])
        self.assertEqual(rps.playerList("Jack", ["Natsu", "Gray", "Carla"]), ["Natsu", "Gray", "Carla", "Jack"])
        self.assertEqual(rps.playerList("Edward", ["Joyce", "Cheng", "Jason"]), ["Joyce", "Cheng", "Jason", "Edward"])
        self.assertEqual(rps.playerList("Justin", ["Tomato", "Salad"]), ["Tomato", "Salad", "Justin"])
        self.assertEqual(rps.playerList("Web", ["Spider", "Man", "Code", "Trash", "Garbage"]), ["Spider", "Man", "Code", "Trash", "Garbage", "Web"])


if __name__ == '__main__':
    unittest.main()