import unittest
from armstrong_numbers import find_armstrong_numbers

class TestArmstrongNumbers(unittest.TestCase):
    def test1(self):
        """0 should return 0"""
        self.assertEqual(find_armstrong_numbers([0]), [0])

    def test2(self):
        """0, 8 should return 0, 1, 2, 3, 4, 5, 6, 7"""
        self.assertEqual(find_armstrong_numbers(
            list(range(0, 8))), [0, 1, 2, 3, 4, 5, 6, 7])

    def test3(self):
        """0, 100 should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
        self.assertEqual(find_armstrong_numbers(list(range(0, 100))), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test4(self):
        """0, 999 should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]"""
        self.assertEqual(find_armstrong_numbers(list(range(0, 999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

    def test5(self):
        """1000, 9999 should return [1634, 8208, 9474]"""
        self.assertEqual(find_armstrong_numbers(list(range(1000, 9999))), [1634, 8208, 9474])

    def test6(self):
        """10000, 99999 should return [54748, 92727, 93084]"""
        self.assertEqual(find_armstrong_numbers(list(range(10000, 99999))), [54748, 92727, 93084])    
    
    def test7(self):
        """100000, 999999 should return [548834]"""
        self.assertEqual(find_armstrong_numbers(list(range(100000, 999999))), [548834])    

if __name__ == '__main__':
    unittest.main()
