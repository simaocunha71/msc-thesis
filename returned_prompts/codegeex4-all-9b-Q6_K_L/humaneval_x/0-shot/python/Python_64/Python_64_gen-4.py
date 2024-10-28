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
    if len(s) == 0:
        return 0
    elif s[-1] == 'y':
        return vowels_count(s[:-1]) + 1
    elif s[-1] in 'aeiouAEIOU':
        return vowels_count(s[:-1]) + 1
    else:
        return vowels_count(s[:-1])
