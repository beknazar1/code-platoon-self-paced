import random
import string


class BoggleBoard:
    dice = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST",
            "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]

    def __init__(self):
        self.row0 = ["_", "_", "_", "_"]
        self.row1 = ["_", "_", "_", "_"]
        self.row2 = ["_", "_", "_", "_"]
        self.row3 = ["_", "_", "_", "_"]

    def shake(self):
        fresh_dice = self.dice.copy()
        random.shuffle(fresh_dice)
        self.row0 = [random.choice(fresh_dice.pop()) for letter in range(4)]
        self.row1 = [random.choice(fresh_dice.pop()) for letter in range(4)]
        self.row2 = [random.choice(fresh_dice.pop()) for letter in range(4)]
        self.row3 = [random.choice(fresh_dice.pop()) for letter in range(4)]
        self.replace_q_in_row(self.row0)
        self.replace_q_in_row(self.row1)
        self.replace_q_in_row(self.row2)
        self.replace_q_in_row(self.row3)

    def get_letter(self):
        return random.choice(string.ascii_uppercase)

    def print_board(self):
        print("".join(l.ljust(3) for l in self.row0))
        print("".join(l.ljust(3) for l in self.row1))
        print("".join(l.ljust(3) for l in self.row2))
        print("".join(l.ljust(3) for l in self.row3))

    def replace_q_in_row(self, row):
        try:
            index = row.index('Q')
            row.pop(index)
            row.insert(index, 'Qu')
        except ValueError:
            pass
