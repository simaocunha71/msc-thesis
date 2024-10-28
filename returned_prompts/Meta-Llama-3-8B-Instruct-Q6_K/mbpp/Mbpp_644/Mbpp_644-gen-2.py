```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```


The function `reverse_Array_Upto_K` takes two parameters, `arr` which is the input array and `k` which is the position up to which the array needs to be reversed. 

The function returns a new array where the elements up to the position `k` are reversed and the remaining elements are kept in the same order. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function is working correctly. 

For example, if the input array is `[1, 2, 3, 4, 5, 6]` and the position is `4`, the function should return `[4, 3, 2, 1, 5, 6]`. 

This function works by slicing the array into two parts at the position `k`, reversing the first part, and then concatenating the two parts. 
```
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))  # [4, 3, 2, 1, 5, 6]
``` 
This function has a time complexity of O(n), where n is the length of the input array. This is because slicing and concatenating arrays in python has a linear time complexity. The space complexity is also O(n) as we are creating a new array. 





```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
``` 
This function takes two parameters, `arr` which is the input array and `k` which is the position up to which the array needs to be reversed. 

The function returns a new array where the elements up to the position `k` are reversed and the remaining elements are kept in the same order. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function is working correctly. 

For example, if the input array is `[1, 2, 