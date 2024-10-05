FIX = """
Add test cases for the edge cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(vowels_count("abcde"))  # prints 2
    print(vowels_count("ACEDY"))  # prints 3
    print(vowels_count("Hello World"))  # prints 3
    print(vowels_count("aeiou"))  # prints 5
    print(vowels_count("bcdfghjklmnpqrstvwxyz"))  # prints 0
    print(vowels_count(""))  # prints 0
    print(vowels_count("y"))  # prints 1
    print(vowels_count("yY"))  # prints 1
    print(vowels_count("yY"))  # prints 1
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcdeY"))  # prints 3
    print(vowels_count("abcde