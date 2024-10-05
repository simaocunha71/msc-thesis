
from collections import Counter


def vowels_count(s):
    vowels = "aeiouy"
    return sum(1 for char in s if char in vowels)


# These passing tests should not be deleted
import doctest
from textwrap import dedent

def main():
    doctest.testmod()
    print(dedent("""
    >> vowels_count("abcde")
        2
    >> vowels_count("ACEDY")
        3
    """))

if __name__ == "__main__":
    main()

"""

"""


FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vow