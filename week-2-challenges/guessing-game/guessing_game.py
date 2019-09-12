# Let's create a simple guessing game. Think in terms of when you were 7 and asked your friends to identify the number you were thinking.

# Your GuessingGame class should be initialized with an integer called something like answer or answer_number.

# Define an instance method GuessingGame#guess (hashtags in documentation generally means it is a method. In our case, GuessingGame has a method called guess) which takes an integer called user_guess as its input. #guess should return the string high if the user_guess is larger than the answer, correct if the user_guess is equal to the answer, and low if the user_guess is lower than the answer.

# Define an instance method GuessingGame#solved which returns True if the most recent user_guess was correct and False otherwise.


class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.isSolved = False

    def guess(self, user_guess):
        if int(user_guess) > self.answer:
            self.isSolved = False
            return "high"
        elif int(user_guess) < self.answer:
            self.isSolved = False
            return "low"
        elif int(user_guess) == self.answer:
            self.isSolved = True
            return "correct"

    def solved(self):
        return self.isSolved
