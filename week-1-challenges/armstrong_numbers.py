import math

def find_armstrong_numbers(numbers):
    OUTPUT = []
    for number in numbers:
        # Leverage python libraries to easily split a number into a list of digits
        DIGITS = [int(digit) for digit in str(number)]
        # Length of DIGITS list will be the exponent per defintion of Armstrong numbers
        power = len(DIGITS)
        # Leverage python again, to calculate sum of powers
        armstrongCandidate = sum([math.pow(digit, power) for digit in DIGITS])
        if armstrongCandidate == number:
            OUTPUT.append(int(armstrongCandidate))
                
    return OUTPUT