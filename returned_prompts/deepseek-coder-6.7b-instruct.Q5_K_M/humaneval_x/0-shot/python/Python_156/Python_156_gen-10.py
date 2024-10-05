
    roman_numeral_dict = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
                          50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}

    roman_numeral = ''
    for key in sorted(roman_numeral_dict.keys(), reverse=True):
        while number >= key:
            roman_numeral += roman_numeral_dict[key]
            number -= key
    return roman_numeral


if __name__ == '__main__':
    import doctest
    doctest.testmod()

This code takes an integer and translates it into the corresponding roman numeral. It does so by iterating over the dictionary, starting from the largest key (1000, 'm'), and subtracting it from the number as long as it's possible. The corresponding roman numeral is added to the string. This process is repeated for the next largest key and so on until the number is 0.

After running the code, the function returns the corresponding roman numeral as a string.

The doctest.testmod() function is used to validate the function's correctness by running the examples provided in the docstring.
'''

#tests.py
import unittest
from mini_roman import int_to_mini_roman


class TestMiniRoman(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')


if __name__ == '__main__':
    unittest.main()

#tests_coverage.py
import unittest
from mini_roman import