    array_copy = array.copy()
    if sum(array[0], array[-1]) % 2 == 0:
        array_copy.sort(reverse=True)
    else:
        array_copy.sort()
    return array_copy
# This function first creates a copy of the input array. Then it checks if the sum of the first and last element is even or odd. If it's even, it sorts the array in descending order, otherwise in ascending order. Finally, it returns the sorted array copy. Note that this function does not modify the original array. It's a good practice to use .copy() to ensure the original array remains unchanged.  # noqa: E501
# https://www.codewars.com/kata/5a3ac9b2f5f5e9f5f3000041/train/python  # noqa: E501
# This is a solution for a coding challenge. It's a good practice to add comments to explain the code. # noqa: E501
# The function takes an array of non-negative integers as input. # noqa: E501
# It returns a copy of the input array after sorting it in either ascending or descending order. # noqa: E501
# The sorting order is determined by the sum of the first and last element of the array. # noqa: E501
# If the sum is even, the array is sorted in descending order. If the sum is odd, the array is sorted in ascending order. # noqa: E501
# The function does not modify the original array. It creates a copy of the array and sorts the copy. # noqa: E501
# This is a good practice to avoid modifying the original array. # noqa: E501
# The function uses the built-in sort method of Python lists to sort the array. # noqa: E501
# The sort method sorts the array in ascending order by default. # noqa: E501
# To sort the array in descending order, we pass the reverse=True argument to the sort method. # noqa: E501
# The function returns the sorted array copy. # noqa: E501
# This is the solution for the coding challenge. # noqa: E501
# It's a good practice to test the function with different inputs to ensure it works correctly. # noqa: E501
# You can use the built-in assert statement to test the function. # noqa: E501
# For example, you can use the following code to test