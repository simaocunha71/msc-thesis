```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```
This function takes an array and an integer k as input. It returns a new array where the elements up to the kth position are reversed, and the rest of the elements remain the same. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function works correctly. 

In the given unit test, the array is [1, 2, 3, 4, 5, 6] and k is 4. The function should return [4, 3, 2, 1, 5, 6], which is the expected output. 

This function uses slicing to divide the array into two parts: the first part up to the kth position and the rest of the array. It then reverses the first part using slicing with a step of -1 and concatenates the two parts to get the final result. 





