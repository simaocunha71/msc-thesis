"""
Write a function to check if a string is present as a substring in a given list of string values.
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
"""
import re

def find_substring(list, value):
    substring = f'{value}'
    for item in list:
        if substring in str(item).lower():
            return True
    return False

if __name__ == '__main__':
    print('find_substring({!r}, "orange")'.format("orange"))