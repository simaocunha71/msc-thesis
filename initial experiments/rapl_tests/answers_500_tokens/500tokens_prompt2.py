
FIX = """
Add more test cases.
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
    vowels = 0
    for c in s:
        if c == "y":
            continue # y at the end of a word is a vowel.
        elif ord(c) == 'a' or ord(c) == 'e' or ord(c) == 'i' or ord(c) == 'o':
            vowels += 1
    return vowels

def main():
    """Write a function flip_vowels which takes a string representing
    a word as input and returns the same string, but with all the
    vowels in reverse order. Note that the reversing is done in place!

    Example:
    >>> w = 'helloworld'
    >>> print flip_vowels(w) # hellowrld
    """
    vowels = set(frozenset("aeiouy"))
    for c in w[::-1]: # reverse the letters, one at a time.
        if ord(c) not in vowels: continue # any non-vowel is fine
    return ''.join(w[::-1])
