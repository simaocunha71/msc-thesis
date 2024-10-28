```
def reverse_Array_Upto_K(arr,k):
    return arr[:k][::-1]+arr[k:]
```


Explanation:
The function `reverse_Array_Upto_K` takes two parameters, `arr` which is the input array and `k` which is the position up to which the array should be reversed. 

It uses Python's list slicing feature to split the array into two parts, the first part from the start to `k` and the second part from `k` to the end. It then reverses the first part using slicing with a step of `-1` and concatenates the two parts to get the final result. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` demonstrates that the function works correctly. It checks that the array `[1, 2, 3, 4, 5, 6]` is reversed up to the position `4` resulting in the array `[4, 3, 2, 1, 5, 6]`. 

The time complexity of this function is O(n) where n is the length of the input array. This is because it needs to access each element of the array once. The space complexity is O(n) as well, as it needs to store the reversed array. 