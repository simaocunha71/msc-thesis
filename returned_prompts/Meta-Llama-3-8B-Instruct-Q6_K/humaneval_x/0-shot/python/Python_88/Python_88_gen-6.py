```
def sort_array(array):
    if len(array) == 0:
        return []

    total_sum = array[0] + array[-1]
    if total_sum % 2 == 0:
        array = sorted(array, reverse=True)
    else:
        array = sorted(array)
    return array.copy()
```



This function takes an array of non-negative integers as an argument. It first checks if the array is empty. If it is, the function returns an empty array.

Next, it calculates the sum of the first and last elements of the array. If the sum is even, it sorts the array in descending order. If the sum is odd, it sorts the array in ascending order.

Finally, the function returns a copy of the sorted array, leaving the original array unchanged. The `copy()` method is used to create a copy of the sorted array, as the function is asked to return a copy of the array rather than modifying the original array. The `sorted()` function is used to sort the array, with the `reverse=True` argument used to sort in descending order. If the sum of the first and last elements is odd, the `sorted()` function is used without any arguments, which sorts the array in ascending order. 





Example outputs:

```
print(sort_array([]))  # Output: []
print(sort_array([5]))  # Output: [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # Output: [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Output: [6, 5, 4, 3, 2, 1, 0]
```





The function works correctly for the given examples. It correctly sorts the array in ascending or descending order based on the sum of the first and last elements, and returns a copy of the sorted array without modifying the original array. 





However, this function assumes that the input array is not empty and that it contains at least one element. If the input array is empty, the function will return an empty array. If the input array contains no elements, the function will raise an IndexError when trying to access the first and last elements. You may want to add error handling to handle these cases.