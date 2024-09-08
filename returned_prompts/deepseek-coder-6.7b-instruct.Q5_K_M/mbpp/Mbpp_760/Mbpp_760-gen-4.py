def vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(vowels("hello world")) # Returns: 3

"""
Write a Python function that takes a string and returns a string with the words in reverse order.
assert