```
def sort_array(array):
    if not array:
        return []
    
    first_index_value = array[0]
    last_index_value = array[-1]
    total = first_index_value + last_index_value
    if total % 2 == 0:
        array = sorted(array, reverse=True)
    else:
        array = sorted(array)
    
    return array
```


Explanation:
We first check if the array is empty, if so, we simply return an empty array. 

Then we calculate the sum of the first and last elements of the array.

If the sum is even, we sort the array in descending order using the sorted function with the reverse parameter set to True.

If the sum is odd, we sort the array in ascending order using the sorted function without the reverse parameter.

Finally, we return the sorted array. 

Note: The original array is not changed, as required. A copy of the array is sorted and returned. 
This is because the sorted function returns a new list and does not modify the original list. 
This is a common pattern in Python, where functions that modify data return the modified data, 
leaving the original data unchanged. 
This is in contrast to some other languages, where functions may modify the original data. 