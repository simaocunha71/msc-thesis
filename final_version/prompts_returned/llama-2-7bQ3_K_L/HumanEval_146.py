
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    return sum(filter(lambda x: (x>=1 and (int(x)%2)*2==1),nums))
print("The number of odd numbers in the array is:", specialFilter([-73, -15, -45, 109]))

# https://www.programiz.com/python-programming/examples/specialfilter