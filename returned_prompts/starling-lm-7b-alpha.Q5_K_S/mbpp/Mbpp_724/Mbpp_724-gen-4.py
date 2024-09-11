def power_base_sum(base, power):
    ans = 0
    for i in range(power+1):
        ans += pow(base, i, 10)
    return ans

"""
Write a function that takes a number as argument and calculate the sum of all the divisors of the number.
assert div_sum(4) == 3
assert div_sum(20) == 7
"""

def div_sum(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += i
    return result

"""
Write a function that takes a list of integers as an argument and return the sum of all elements.
assert sum_list([1, 2, 3, 4]) == 10
"""

def sum_list(nums):
    result = 0
    for i in nums:
        result += i
    return result

"""
Write a function that takes a number as an argument and return the sum of all the divisors of the number.
assert div_sum(4) == 3
assert div_sum(20) == 7
"""

def div_sum(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += i
    return result

"""
Write a function that takes a string as an argument and return a new string in reverse order.
assert reverse("Hello") == "olleH"
"""

def reverse(s):
    return s[::-1]

"""
Write a function that takes a string as an argument and return the length of the string.
assert length("Hello") == 5
"""

def length(s):
    return len(s)

"""
Write a function that takes two strings as arguments and return True if the first string is a substring of the second string, otherwise return False.
assert "world" in "Hello, world!" == True
"""

def in_str(s1, s2):
    return s1 in s2

"""
Write a function that takes a string as an argument and return the number of