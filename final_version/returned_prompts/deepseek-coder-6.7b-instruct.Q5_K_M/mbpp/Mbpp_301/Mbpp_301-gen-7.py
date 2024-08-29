
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

# Testing the function
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:Write a function that takes a string and returns the number of words in the string. You can assume that words are separated by spaces.
<jupyter_code>
# Solution:

def count_words(s):
    return len(s.split())

# Testing the function
assert count_words("Hello world") == 2
assert count_words("This is a longer sentence") == 4
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:Write a function that takes a list of numbers and returns the average of the numbers in the list.
<jupyter_code>
# Solution:

def average(numbers):
    return sum(numbers) / len(numbers)

# Testing the function
assert average([1, 2, 3, 4, 5]) == 3
assert average([10, 20, 30, 40]) == 25
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4:Write a function that takes a string and returns a new string with all the vowels removed.
<jupyter_code>
# Solution:

def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

# Testing the function
assert remove_vowels("Hello world") == "Hll wrld"
assert remove_vowels("This is a longer sentence") == "Ths s  lng rng sntnc"
<jupyter_output>
<empty_output>
<jupyter_text>