
    roman_numerals = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i')
    ]

    result = ""

    for value, numeral in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

#tests.py
import unittest
from mini_roman_numerals import int_to_mini_roman

class TestMiniRomanNumerals(unittest.TestCase):

    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == "__main__":
    unittest.main()

#time_complexity.py
from timeit import timeit
from mini_roman_numerals import int_to_mini_roman

if __name__ == "__main__":
    for num in [1, 10, 100, 1000]:
        print(f"Number: {num} - Time: {timeit(lambda: int_to_mini_roman(num), number=10000)}")

# 1: 0.00006210000000001459
# 10: 0.000