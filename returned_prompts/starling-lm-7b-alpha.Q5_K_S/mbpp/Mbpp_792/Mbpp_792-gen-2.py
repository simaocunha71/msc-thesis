def count_list(lists):
    return len(lists)


def test_count_list():
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4


test_count_list()


"""
Write a python function to multiply two numbers
"""

def multiply(num1, num2):
    return num1 * num2


def test_multiply():
    assert multiply(2, 3) == 6


test_multiply()


"""
Write a python function to add two numbers
"""

def add(num1, num2):
    return num1 + num2


def test_add():
    assert add(2, 3) == 5


test_add()


"""
Write a python function to find the maximum number between two numbers
"""

def max_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def test_max_num():
    assert max_num(2, 3) == 3


test_max_num()


"""
Write a python function to find the minimum number between two numbers
"""

def min_num(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


def test_min_num():
    assert min_num(2, 3) == 2


test_min_num()


"""
Write a python function to check if a string is a substring of another string
"""

def substring(str1, str2):
    if str2 in str1:
        return True
    else:
        return False


def test_substring():
    assert substring('hello world', 'world') == True
    assert substring('hello world', 'foo') == False


test_substring()


"""
Write a python function to check if a string is a palindrome
"""

def palindrome(str1):
