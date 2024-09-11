def check_monthnumber_number(month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return False
    return month_days[month-1] == 30


# Testing
print(check_monthnumber_number(6))  # True
print(check_monthnumber_number(2))  # False

"""
Here, We have a function check_monthnumber_number(month) that checks if the given month number contains 30 days or not. It returns True if the month has 30 days and False if it does not.
In the function, we create a list called month_days containing the number of days in each month (31 days for most months, 28 for February, and 30 for April, June, September and November). We then check if the month is within the valid range (1 to 12). If the month is not valid, we return False. Otherwise, we return True if the number of days for the given month is 30, and False otherwise.
"""

# Python3 program to find
# number of set bits in an
# integer


def setBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


# Driver Code
x = 31
print(setBits(x))

"""
Here, We have a function called setBits(n) that counts the number of set bits in an integer. It returns the count of set bits.
In the function, we initialize a variable count to 0. Then, we enter a while loop that continues until n becomes 0. In each iteration of the loop, we increment the count by 1 if the least significant bit of n is set (i.e., if n & 1 is true). Then, we right-shift n by 1 bit to move to the next bit. This process continues until n becomes 0. Finally, we return the count of set bits.
"""

# Python program to find