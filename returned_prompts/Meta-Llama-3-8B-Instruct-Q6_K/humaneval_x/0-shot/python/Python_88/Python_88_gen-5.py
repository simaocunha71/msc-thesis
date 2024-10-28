```
def sort_array(array):
    if len(array) == 0:
        return []

    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
```

Explanation:
The function `sort_array` takes an array of non-negative integers as input and returns a copy of the given array after sorting. 

First, it checks if the array is empty. If it is, the function returns an empty array.

Then, it calculates the sum of the first and last elements of the array. 

If the sum is even, the function sorts the array in descending order using the `sorted` function with the `reverse` argument set to `True`.

If the sum is odd, the function sorts the array in ascending order using the `sorted` function without the `reverse` argument.

The function does not change the original array and returns a copy of the sorted array. 

The function handles edge cases such as an empty array, an array with a single element, and arrays with multiple elements. It also handles the cases where the sum of the first and last elements is even or odd. 

The function is efficient and has a time complexity of O(n log n) due to the use of the `sorted` function, where n is the length of the array. The space complexity is O(n) for the sorted array. 