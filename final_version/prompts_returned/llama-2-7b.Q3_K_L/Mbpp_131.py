"""
Write a python function to reverse only the vowels of a given string (where y is not a vowel).
assert reverse_vowels("Python") == "Python"
"""
#!/bin/python3
import re

def reverseVowels(sentence):
    return re.sub('[AEIOU]', '', sentence)
print (reverseVowelp("Python"))