def test_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1))  # 3
print(test_three_equal(1,2,1))  # 2
print(test_three_equal(1,2,3))  # 0

"""
Write a python function to check if a number is a power of two.
assert test_power_of_two(1) == True
assert test_power_of_two(2) == True
assert test_power_of_two(3) == False
"""

def test_power_of_two(n):
    while n > 1:
        n /= 2
    return n == 1

print(test_power_of_two(1))  # True
print(test_power_of_two(2))  # True
print(test_power_of_two(3))  # False

"""
Write a python function to check if a given year is a leap year or not.
assert test_leap_year(2000) == True
assert test_leap_year(1900) == False
assert test_leap_year(2004) == True
"""

def test_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(test_leap_year(2000))  # True
print(test_leap_year(1900))  # False
print(test_leap_year(2004))  # True

"""
Write a python function to find the maximum and minimum numbers from three given integers.
assert test_max_min(1,2,3) == (3,1)
"""

def test_max_min(a