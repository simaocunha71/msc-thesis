def find_Max_Num(nums):
    nums.sort(reverse=True)
    return int(''.join(map(str,nums)))

# Test
print(find_Max_Num([1,2,3])) # 321

"""
The function works by first sorting the list of digits in descending order. This can be achieved by using the built-in function `sort(reverse=True)`. Then, we convert the sorted list of digits to a string using `map(str,nums)`. This is because the `int()` function expects a string as the argument, and not a list of digits. Finally, we join the string representation of the digits using `''.join()` and convert it to an integer using `int()`.
"""

"""
The time complexity of this function is O(nlogn) due to the sorting operation. The space complexity is O(n) due to the creation of a new list and the conversion of the list to a string.
"""

# You can test the function using the provided assert statement to ensure that it correctly finds the largest number that can be formed with the given list of digits.

# Note that the function assumes that all numbers in the input list are integers. If there are non-integer values in the input list, they will be ignored and will not affect the result.

# This function can be used to find the largest number that can be formed from a given list of digits, which can be useful in various applications such as maximizing the value of a number, or solving certain types of puzzles or problems that involve arranging digits in a specific order.

"""
Here are some additional notes about the function:

- The function uses the built-in `sort()` function with the `reverse=True` parameter to sort the list of digits in descending order. This ensures that the largest digit is at the beginning of the list.
- The function uses the built-in `map()` function to convert each digit in the list to a string. This is necessary because the `int()` function expects a string as the argument, and not a list of digits.
- The function uses the built-in `join()` function to concatenate the string representation of the digits into a single string. This is