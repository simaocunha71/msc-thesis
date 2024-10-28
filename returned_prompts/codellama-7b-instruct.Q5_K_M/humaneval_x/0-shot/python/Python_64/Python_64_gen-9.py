
    return sum(s.count(vowel) for vowel in "aeiou" if vowel in s)

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
    for char in s:
        if char in "aeiouy" and char != "y":
            vowels += 1
        elif char == "y":
            if s[len(s)-1] == "y":
                vowels += 1

    return vowels