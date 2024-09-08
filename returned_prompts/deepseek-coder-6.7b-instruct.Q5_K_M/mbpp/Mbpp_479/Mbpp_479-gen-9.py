def count_Digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

print(count_Digits(123))

# output: 3

# Q6:
"""
Write a python function to check if a given number is a palindrome.
assert is_Palindrome(123) == False
assert is_Palindrome(121) == True
"""

A