def next_power_of_2(n):
    if n==0:
        return 1
    else:
        while n%2!=1:
            n = n*2
    return n

# Testing
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 2
assert next_power_of_2(3) == 4
assert next_power_of_2(6) == 8
assert next_power_of_2(9) == 8
assert next_power_of_2(15) == 16

print("All tests passed.")




"""
Write a Python function to find the smallest power of 2 greater than or equal to n.

Examples:
next_power_of_2(0) ➞ 1
next_power_of_2(1) ➞ 2
next_power_of_2(3) ➞ 4
next_power_of_2(6) ➞ 8
next_power_of_2(9) ➞ 8
next_power_of_2(15) ➞ 16
"""




"""
Given two strings, write a function to determine if the second string is a rotation of the first. In other words, if the second string is obtained by moving the first string's characters to a different position in the string, then the second string is a rotation of the first string.

Examples:

rotated_string("waterbottle", "erbottlewat") ➞ True
rotated_string("example", "ampleex") ➞ True
rotated_string("test", "sett") ➞ True
rotated_string("test", "ested") ➞ False
"""

def rotated_string(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i:] + s1[:i] == s2:
                return True
        return