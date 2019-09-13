import unittest
from boggle_board import BoggleBoard


class BoggleBoardTests(unittest.TestCase):
    boggle = BoggleBoard()

    def test_get_letter_returns_upper(self):
        for n in range(20):
            self.assertTrue(self.boggle.get_letter().isupper())

    def test_row_lengths(self):
        self.assertEqual(len(self.boggle.row0), 4)
        self.assertEqual(len(self.boggle.row1), 4)
        self.assertEqual(len(self.boggle.row2), 4)
        self.assertEqual(len(self.boggle.row3), 4)

    def test_shake(self):
        row_0_copy = self.boggle.row0
        row_1_copy = self.boggle.row1
        row_2_copy = self.boggle.row2
        row_3_copy = self.boggle.row3
        self.boggle.shake()
        self.assertNotEqual(row_0_copy, self.boggle.row0)
        self.assertNotEqual(row_1_copy, self.boggle.row1)
        self.assertNotEqual(row_2_copy, self.boggle.row2)
        self.assertNotEqual(row_3_copy, self.boggle.row3)

    def test_q(self):
        die = ['A', 'Q', 'C', 'D']
        self.boggle.replace_q_in_row(die)
        self.assertEqual(die, ['A', 'Qu', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
