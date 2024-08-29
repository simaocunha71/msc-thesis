def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

# OR

def move_zero(lst):
    return lst.sort(key=lambda x: x == 0)
    return lst

print(move_zero([1,0,2,0,3,4]))

# OR

def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

# OR

def move_zero(lst):
    count = lst.count(0)
    return [i for i in lst if i != 0] + [0]*count

print(move_zero([1,0,2,0,3,4]))
<jupyter_output>
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a Python function to check whether a given string is a pangram or not.
A pangram is a sentence containing every letter in the English Alphabet.

Example:
    Input: The quick brown fox jumps over the lazy dog
    Output: True
"""

def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

print(pangram("The quick brown fox jumps over the lazy dog"))
<jupyter_output>
True
<jupyter_text>
Q