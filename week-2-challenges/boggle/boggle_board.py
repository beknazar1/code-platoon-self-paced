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

    def include_word(self, word):
        word = word.upper()
        # Flatten lists into a single list for easier iteration
        nested_array = [self.row0, self.row1, self.row2, self.row3]
        flat_array = []
        for list in nested_array:
            for letter in list:
                flat_array.append(letter)

        # call a helper recursive function to look for possible match
        return self.recursive_include_word(flat_array, word)
        

        # Find all occurences of word's first character, in case of multiple starting points
        # when character is found - replace character with a filler character and check adjacent letters
        # N(-4), NE(-3), E(+1), SE(+5), S(+4), SW(+3), W(-1), NW(-5)
        # return True when word is empty
    def recursive_include_word(self, flat_array, word):
        print(f"looking for word {word}")
        if len(word) == 0:
            print('Gotcha')
            return True
        
        character_occurence_index = []
        for i in range(len(flat_array)):
            if word[0] == flat_array[i] or (word[:2] == 'QU' and flat_array[i] == 'Qu'):
                character_occurence_index.append(i)

        for index in character_occurence_index:
            new_flat_array = flat_array.copy()
            character = new_flat_array.pop(index)
            new_flat_array.insert(index, "_")
            print(f"new flat array is {new_flat_array}")
            found = self.recursive_include_word(new_flat_array, word[len(character):])
            if found:
                return True