from collections import Counter
def test_duplicate(nums):
    return len(Counter(nums)) != len(nums)

"""
Write a function that takes a string and returns a dictionary where the keys are the characters from the string, and the values are the number of times the character appears in the string.

assert count_characters("") == {}
assert count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""

def count_characters(string):
    return {char:string.count(char) for char in string}

"""
Write a function to calculate the sum of all the elements in a given array of integers.

assert sum_of_integers([1,2,3,4,5]) == 15
"""

def sum_of_integers(nums):
    return sum(nums)

"""
Write a function that takes a string and returns a dictionary where the keys are the characters from the string, and the values are the number of times the character appears in the string.

assert most_common_character("") == {}
assert most_common_character("hello") == {'l': 2, 'o': 2, 'h': 1, 'e': 1}
"""

from collections import Counter
def most_common_character(string):
    return Counter(string).most_common(1)[0][0]

"""
Write a function that takes a string and returns a dictionary where the keys are the characters from the string, and the values are the number of times the character appears in the string.

assert most_common_character("") == {}
assert most_common_character("hello") == {'l': 2, 'o': 2, 'h': 1, 'e': 1}
"""
from collections import Counter
def most_common_character(string):
    return Counter(string).most_common(1)[0][0]

"""
Write a function that takes a string and returns a dictionary where the keys are the characters from the string, and the values are the number of times the character appears in the string.

assert most_common_character("")