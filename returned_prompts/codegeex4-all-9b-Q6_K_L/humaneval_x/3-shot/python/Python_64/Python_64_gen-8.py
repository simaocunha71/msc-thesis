    s = s.lower()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    if s[-1] == 'y':
        count += 1

    for c in s:
        if c in vowels:
            count += 1

    return count

FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u