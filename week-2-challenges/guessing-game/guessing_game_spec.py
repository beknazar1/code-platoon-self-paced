import unittest
from guessing_game import GuessingGame


class GuessingGameTest(unittest.TestCase):
    """
    Set up the class instance first
    """
    game = GuessingGame(10)

    def test_high(self):
        """Guessing higher number should return 'high'"""
        self.assertEqual(self.game.guess(15), "high")

    def test_low(self):
        """Guessing higher number should return 'low'"""
        self.assertEqual(self.game.guess(5), "low")

    def test_is_not_solved(self):
        """Test that solved is False"""
        self.game.guess(1)
        self.assertFalse(self.game.solved())

    def test_correct(self):
        """Guessing higher number should return 'low'"""
        self.assertEqual(self.game.guess(10), "correct")

    def test_is_not_solved(self):
        """Test that solved is False"""
        self.game.guess(1)
        self.assertFalse(self.game.solved())

    def test_is_solved(self):
        """Test that solved is True"""
        self.game.guess(10)
        self.assertTrue(self.game.solved())


if __name__ == '__main__':
    unittest.main()
