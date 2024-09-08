def split(word):
    return [char for char in word]

print(split('python'))


#Q2:
"""
Write a python function to count the number of occurrences of each character in a string.
assert char_count('hello') == {'h':1, 'e':1, 'l':2, 'o':1}
"""

A2:
def char_count(str1):
    dict1 = {}
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1

print(char_count('hello'))


#Q3:
"""
Write a Python function that checks if a string is a palindrome (the same read backwards as forward).
assert is_palindrome('radar') == True
assert is_palindrome('python') == False
"""

A3:
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('radar'))
print(is_palindrome('python'))


#Q4:
"""
Write a Python function that checks if a string is a pangram (contains every letter of the alphabet at least once).
assert is_pangram('The quick brown fox jumps over the lazy dog') == True
assert is_pangram('Hello World') == False
"""

A4:
def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('Hello World'))


#Q5:
"""
Write a Python function that returns the number of words in a string.
assert count_words('Hello, World') == 2
"""

A5:
def count_words(string):
    return len(string.split())

print(count_words('Hello,