```
def kth_element(arr, k):
    k -= 1  # adjust for 0-based indexing
    return arr[k]
```
This function takes an array and an integer k as input. It subtracts 1 from k to adjust for 0-based indexing and then returns the element at the kth index in the array.

The unit test `assert kth_element([12,3,5,7,19], 2) == 3` confirms that the function works correctly. It checks that the 2nd element (1-based indexing) in the array [12,3,5,7,19] is 3, which is the expected output.