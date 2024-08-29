
def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

print(count_vowels("hello world"))

"""
Write a Python function that takes a list of numbers and returns