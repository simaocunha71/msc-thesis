def count_charac(s):
    count = 0
    for i in s:
        count += 1
    return count

assert count_charac("python programming")==18

"""
Write a function to count the total number of vowels in a string.
assert count_vowel("python programming")==7
"""
def count_vowel(s):
    vowels = "aeiou"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

assert count_vowel("python programming")==7

"""
Write a function to count the total number of consonants in a string.
assert count_consonant("python programming")==9
"""
def count_consonant(s):
    vowels = "aeiou"
    count = 0
    for i in s:
        if i not in vowels:
            count += 1
    return count

assert count_consonant("python programming")==9

"""
Write a function to count the total number of spaces in a string.
assert count_space("python programming")==2
"""
def count_space(s):
    count = 0
    for i in s:
        if i == " ":
            count += 1
    return count

assert count_space("python programming")==2

"""
Write a function to count the total number of upper case characters in a string.
assert count_upper("Python Programming")==7
"""
def count_upper(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for i in s:
        if i in upper:
            count += 1
    return count

assert count_upper("Python Programming")==7

"""
Write a function to count the total number of lower case characters in a string.
assert count_lower("python programming")==11
"""
def count_lower(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in