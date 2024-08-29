
def opposite_Signs(n1, n2): 
    return (n1 ^ n2) < 0

print(opposite_Signs(1,-2)) # True

Explanation:
In this function, we are using the bitwise XOR operator (^). If two numbers have the same sign, the result of the bitwise XOR operation will be negative. If the numbers have different signs, the result will be positive. Thus we return true if result is less than 0.

Note:
The bitwise XOR operator (^) in python returns a number which has a bit set at the position where the corresponding bits of two numbers are different.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q3. Write a Python function to find the repeated character present first in a string.
<jupyter_code>
def firstRepeatedCharacter(str):
    charCount = {}
    for ch in str:
        if ch in charCount:
            return ch
        else:
            charCount[ch] = 1
    return None

print(firstRepeatedCharacter('abcdea'))  # 'a'
print(firstRepeatedCharacter('abcdeabc'))  # 'a'
<jupyter_output>
a
a
<jupyter_text>
Q4. Write a Python program that will print all the permutations of the given string.
<jupyter_code>
from itertools import permutations

def allPermutations(str):
    perms = permutations(str)
    for perm in perms:
        print(''.join(perm))

allPermutations('abc')
<jupyter_output>
abc
acb
bac
bca
cba
cab
<jupyter_text>
Q5. Write a Python function to check whether a given string is a palindrome or not.
<jupyter_code>
def isPalindrome(str):
    return str == str[::-1]

print(isPalindrome('madam'))  # True
print(isPalindrome('hello'))  # False
<j