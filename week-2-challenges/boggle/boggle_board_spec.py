import unittest
from boggle_board import BoggleBoard


class BoggleBoardTests(unittest.TestCase):
    boggle = BoggleBoard()

    def test_board_lengths(self):
        self.assertEqual(len(self.boggle.board), 16)

    def test_shake(self):
        board_copy = self.boggle.board.copy()
        self.boggle.shake()
        self.assertNotEqual(board_copy, self.boggle.board)

    def test_q(self):
        die = ['A', 'Q', 'C', 'D']
        self.boggle.replace_q_in_row(die)
        self.assertEqual(die, ['A', 'Qu', 'C', 'D'])

    def test_include_horizontal(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("ABCD"))
        self.assertTrue(b.include_word("HGFE"))

    def test_include_vertical(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("AEIM"))
        self.assertTrue(b.include_word("PLHD"))

    def test_include_diagonal(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("AFKP"))
        self.assertTrue(b.include_word("DGJM"))

    def test_include_snake(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("ABFEJOLG"))

    def test_include_repeat_returns_false(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertFalse(b.include_word("ABCDHGCD"))

    def test_include_lower_case(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("abcd"))

    def test_include_disjointed_returns_false(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertFalse(b.include_word("ABCKO"))
        self.assertFalse(b.include_word("DGA"))

    def test_include_requires_3_char_min(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertFalse(b.include_word(""))
        self.assertFalse(b.include_word("A"))
        self.assertFalse(b.include_word("AB"))
        self.assertTrue(b.include_word("ABC"))

    def test_include_word_too_long(self):
        b = BoggleBoard()
        b.board = list('ABCDEFGHIJKLMNOP')
        self.assertTrue(b.include_word("ABCDHGFEIJKLPONM"))
        self.assertFalse(b.include_word("ABCDHGFEIJKLPONMR"))


if __name__ == '__main__':
    unittest.main()
