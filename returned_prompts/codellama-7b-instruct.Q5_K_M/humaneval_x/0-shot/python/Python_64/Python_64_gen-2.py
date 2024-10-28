
    vowels = 0
    for char in s:
        if char in "aeiouy":
            vowels += 1
    return vowels

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
    return sum(1 for c in s if c in "aeiouy" and c != "y" or c == "y" and s[-1] == c)
