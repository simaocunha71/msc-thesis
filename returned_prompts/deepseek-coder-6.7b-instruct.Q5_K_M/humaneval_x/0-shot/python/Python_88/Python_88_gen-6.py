
def sort_array(array):
    if len(array) == 0 or len(array) == 1:
        return array

    if (array[0] + array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

print(sort_array([])) # []
print(sort_array([5])) # [5]
print(sort_array([2, 4, 3, 0, 1, 5])) # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6])) # [6, 5, 4, 3, 2, 1, 0]

This solution first checks if the given array is empty or has only one element. In these cases, the function returns the array as it is.

Then, it checks if the sum of the first and last elements of the array is even. If it is, it returns a sorted version of the array in descending order. If the sum is odd, it returns a sorted version of the array in ascending order.

The sorted() function is used to sort the array, and the reverse parameter is set to True to sort in descending order if the sum is even. If the sum is odd, reverse is set to False, so the array is sorted in ascending order.

The result is a new array that is a copy of the original array but sorted as specified. The original array is not modified.

The time complexity of this solution is O(n log n), because the sorted() function used to sort the array. The space complexity is O(n), because a new array is created to store the sorted elements.

This solution assumes that the array will always contain non-negative integers, as stated in the problem.

The problem does not specify what should happen if the array contains negative numbers or non-integer values. In this solution, the function will not work correctly for these cases.

It's also worth noting that the given array will not be empty when the function is called. In the worst case, the function will always return the array itself. This is because the time complexity of the function is O(n