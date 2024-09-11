def count_Set_Bits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_Set_Bits(n & (n - 1))


"""
Write a function to find the first common element between two lists.

assert common_Element([1, 2, 3, 4], [3, 4, 5, 6]) == 3
"""

def common_Element(list1, list2):
    for elem in list1:
        if elem in list2:
            return elem
    return None


"""
Write a function to convert a string to a number in Python.

assert convert_String_To_Number("123") == 123
"""

def convert_String_To_Number(string):
    if string[0] == "-":
        return -int(string[1:])
    else:
        return int(string)


"""
Write a function to check whether a string is a palindrome or not.

assert is_Palindrome("racecar") == True
"""

def is_Palindrome(string):
    return string == string[::-1]


"""
Write a function to get the first n even numbers.

assert first_n_Even_Numbers(10) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
"""

def first_n_Even_Numbers(n):
    return [i * 2 for i in range(n)]


"""
Write a function to get the first n odd numbers.

assert first_n_Odd_Numbers(10) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""

def first_n_Odd_Numbers(n):
    return [2 * i + 1 for i in range(n)]


"""
Write a function to get a list of prime numbers up to a given number.

assert prime_Numbers_Up_