
def specialFilter(nums):
    count = 0
    for num in nums:
        num_str = str(num)
        if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0 and num > 10:
            count += 1
    return count


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))





# Python3 program to count the number of
# elements in an array which are greater
# than 10 and both the first and last
# digits of the number are odd.

# Function to check if both the first and
# last digit of a number are odd
def isOdd(n):

    # Converting number to string
    # to access the first and last
    # digit of the number
    str_n = str(n)

    # Checking if the first and
    # the last digit of the number
    # are odd or not
    if ((str_n[0] % 2 != 0) and
        (str_n[-1] % 2 != 0)):
        return True
    return False


# Function to count the number of
# elements in an array which are
# greater than 10 and both the
# first and last digit of the
# number are odd
def specialFilter(nums):

    # Initializing count as 0
    count = 0

    # Iterating through all the elements
    # of the array
    for num in nums:

        # If the current element is
        # greater than 10 and both
        # the first and the last
        # digit of the number
        # are odd, increment the
        # count
        if (num > 10 and isOdd(num)):
            count += 1

    return count


# Driver Code
nums = [15, -73, 14, -15, 33, -2, -3, 45,