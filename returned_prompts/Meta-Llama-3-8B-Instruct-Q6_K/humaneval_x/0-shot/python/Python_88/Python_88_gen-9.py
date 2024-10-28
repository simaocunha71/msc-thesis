
Here is the Python code for the solution:
```
def sort_array(array):
    if len(array) == 0:
        return array
    
    total_sum = array[0] + array[-1]
    if total_sum % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)
```
This code works by first checking if the array is empty. If it is, it returns the array as is. Then, it calculates the sum of the first and last elements of the array. If this sum is odd, it returns a sorted copy of the array in ascending order. If the sum is even, it returns a sorted copy of the array in descending order. The `sorted` function is used to sort the array, and the `reverse=True` argument is used to sort the array in descending order if the sum is even.