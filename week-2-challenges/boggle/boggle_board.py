import random
import string


class BoggleBoard:
    dice = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY", "EIOSST",
            "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]

    def __init__(self):
        self.board = ["_"] * 16

    def shake(self):
        fresh_dice = self.dice.copy()
        random.shuffle(fresh_dice)
        self.board = [random.choice(fresh_dice.pop()) for letter in range(16)]
        self.replace_q_in_row(self.board)

    def print_board(self):
        print("".join(l.ljust(3) for l in self.board[0:4]))
        print("".join(l.ljust(3) for l in self.board[4:8]))
        print("".join(l.ljust(3) for l in self.board[8:12]))
        print("".join(l.ljust(3) for l in self.board[12:16]))

    def replace_q_in_row(self, row):
        try:
            index = row.index('Q')
            row.pop(index)
            row.insert(index, 'Qu')
        except ValueError:
            pass

    def include_word(self, word):
        if len(word) < 3:
            return False
        word = word.upper()
        boggle = self.board.copy()
        # Keep track of visited cells to avoid reusing them
        path = []

        # Find all occurences of word's first character, in case of multiple starting points
        character_occurence_index = []
        for i in range(len(boggle)):
            if word[0] == boggle[i] or (word[:2] == 'QU' and boggle[i] == 'Qu'):
                character_occurence_index.append(i)

        # call a helper recursive function to look for possible match
        for index in character_occurence_index:
            new_path = path.copy()
            new_path.append(index)
            found = self.recursive_include_word(
                boggle, word[len(boggle[index]):], new_path)
            if found:
                return True
        else:
            return False

    def recursive_include_word(self, boggle, word, path):
        # N(-4), NE(-3), E(+1), SE(+5), S(+4), SW(+3), W(-1), NW(-5)
        adjacent_cells = [-4, -3, 1, 5, 4, 3, -1, -5]

        # Base Case - return True when word is empty
        if len(word) == 0:
            return True

        for adjacent in adjacent_cells:
            current_index = path[-1]
            adjacent_cell = current_index + adjacent
            # Check adjacent cells if they are legal, and check if they haven't been used in the word yet
            if (adjacent_cell >= 0 and adjacent_cell < 16 and adjacent_cell not in path):
                if word[0] == boggle[adjacent_cell] or (word[:2] == 'QU' and boggle[adjacent_cell] == 'Qu'):
                    # when character is found - add it to visited path
                    new_path = path.copy()
                    new_path.append(adjacent_cell)
                    # Making a recursive call
                    found = self.recursive_include_word(
                        boggle, word[len(boggle[adjacent_cell]):], new_path)
                    if found:  # Checking result of recursion
                        return True
