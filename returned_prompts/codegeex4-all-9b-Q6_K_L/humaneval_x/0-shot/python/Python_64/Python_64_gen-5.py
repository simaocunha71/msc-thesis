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
    for i in s.lower():
        if i in 'aeiou':
            vowels += 1
    if s[-1].lower() == 'y':
        vowels += 1
    return vowels

print(vowels_count('abcde'))
print(vowels_count('ACEDY'))