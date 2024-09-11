def check_greater(arr, num):
    for i in range(len(arr)):
        if arr[i] < num:
            return False
    return True


print(check_greater([1, 2, 3, 4, 5], 4))


"""
The function check_greater(arr, num) takes two parameters: an array arr and a number num. It iterates through the array using a for loop and compares each element to the entered number num. If any element is less than num, the function returns False. If all the elements of the array are greater than the entered number, the function returns True.

In the provided example, the function check_greater([1, 2, 3, 4, 5], 4) is called. The array [1, 2, 3, 4, 5] is passed as the first argument and the number 4 as the second argument. The function checks each element of the array and compares it to 4. The first element 1 is less than 4, so the function returns False.

The assert statement is used to check if the function correctly returns False for the given example. If the function returns True instead of False, the assert statement will raise an AssertionError, indicating that the function is not working correctly.

"""

# Python program to check whether the entered number is greater than the elements of the given array or not

def check_greater(arr, num):
    for i in range(len(arr)):
        if arr[i] < num:
            return False
    return True

# Example usage
print(check_greater([1, 2, 3, 4, 5], 4))  # False
print(check_greater([10, 20, 30, 40, 50], 50))  # True

# Assertion to validate the function
assert check_greater([1, 2, 3, 4, 5], 4) == False

# The function check_greater(arr, num) takes two parameters: an array arr and a number num. It iterates through the array using a for loop and compares each element to the entered number num. If any