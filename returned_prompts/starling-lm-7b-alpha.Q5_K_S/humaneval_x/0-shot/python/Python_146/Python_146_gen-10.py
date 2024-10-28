
def specialFilter(nums):
    """
    Returns the number of elements in the array that are greater than 10 and 
    both first and last digits of a number are odd (1, 3, 5, 7, 9).
    """
    count = 0
    for num in nums:
        if num > 10 and (num % 10) % 2 == 1 and (num // 10) % 10 % 2 == 1:
            count += 1
    return count

# test cases
print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
print(specialFilter([100, 200, 300, 400, 500]))



def specialFilter(nums):
    """
    Returns the number of elements in the array that are greater than 10 and 
    both first and last digits of a number are odd (1, 3, 5, 7, 9).
    """
    count = 0
    for num in nums:
        if num > 10 and (num % 10) % 2 == 1 and (num // 10) % 10 % 2 == 1:
            count += 1
    return count

# test cases
print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
print(specialFilter([100, 200, 300, 400, 500]))
























































































