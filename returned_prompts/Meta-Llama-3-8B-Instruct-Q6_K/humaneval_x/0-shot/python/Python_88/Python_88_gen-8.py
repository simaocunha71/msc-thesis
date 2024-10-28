
The function `sort_array` takes an array of non-negative integers as input. It first checks if the array is empty. If it is, the function returns an empty list.

Next, it calculates the sum of the first and last elements of the array. It then checks if this sum is odd. If it is, the function sorts the array in ascending order using the built-in `sorted` function. If the sum is even, the function sorts the array in descending order using the `sorted` function with the `reverse=True` argument.

Here is the Python code that implements this logic:
```
def sort_array(array):
    if not array:
        return []

    first_last_sum = array[0] + array[-1]
    is_odd = first_last_sum % 2 != 0

    if is_odd:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
```
This function works as expected, and it does not modify the original array. It returns a new sorted array based on the condition specified in the problem statement.