"""
To check whether the entered number is greater than the elements of the given array, you can use the following function:

def check_greater(arr, num):
    for i in arr:
        if i < num:
            return False
    return True

This function takes an array 'arr' and a number 'num' as input. It iterates through each element in the array 'arr' and compares it with the number 'num'. If any element is found to be less than 'num', the function returns False. If all the elements are greater than or equal to 'num', the function returns True.

In the provided assertion, the function is called with the array [1, 2, 3, 4, 5] and the number 4. Since 4 is less than 5, the assertion is True and the function returns False, as expected.
"""

# Python3 program to check if a number is greater than
# all the elements in an array

# Function to check if a number is greater than
# all the elements in an array
def check_greater(arr, num):
    # Traverse through the array
    for i in arr:
        # If any element is found to be less than num
        if i < num:
            return False
    return True

# Driver program
if __name__ == "__main__":
    # The array and the number to be checked
    arr = [1, 2, 3, 4, 5]
    num = 4

    # Check if num is greater than all the elements
    # in the array
    if(check_greater(arr, num)):
        print("True")
    else:
        print("False")


# This code is contributed by mohit1412


# Output:
# False
"""
This code defines a function called 'check_greater' that takes an array 'arr' and a number 'num' as input. It iterates through each element in the array 'arr' and compares it with the number 'num'. If any element is found to be less than 'num', the function returns False. If all the elements are greater than or equal to 'num', the function returns True.

In the provided driver program,