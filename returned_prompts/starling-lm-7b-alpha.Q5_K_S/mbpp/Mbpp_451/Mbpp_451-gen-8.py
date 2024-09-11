def remove_whitespaces(string):
    return string.replace(' ', '')

# assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
# print(remove_whitespaces(' Google    Flutter '))






"""
Write a function to capitalize the first letter of each word in the given string.
assert capitalize_first_letters(' this is a string ') == 'This Is A String '
"""


def capitalize_first_letters(string):
    return ' '.join(x[0].upper() + x[1:] for x in string.split())

# assert capitalize_first_letters(' this is a string ') == 'This Is A String '
# print(capitalize_first_letters(' this is a string '))





"""
Write a function to capitalize all the letters in the given string.
assert capitalize_all_letters(' this is a string ') == 'THIS IS A STRING'
"""

def capitalize_all_letters(string):
    return string.upper()

# assert capitalize_all_letters(' this is a string ') == 'THIS IS A STRING'
# print(capitalize_all_letters(' this is a string '))




"""
Write a function to reverse the given string.
assert reverse_string('this is a string') == 'gnirts a si sihT'
"""

def reverse_string(string):
    return string[::-1]

# assert reverse_string('this is a string') == 'gnirts a si sihT'
# print(reverse_string('this is a string'))




"""
Write a function to count the number of vowels in the given string.
assert count_vowels('this is a string') == 6
"""

def count_vowels(string):
    vowels = "aeiou"
    return sum(1 for c in string if c in vowels)

# assert count_vowels('this is a string') == 6
# print(count_vowels('this is a string'))




