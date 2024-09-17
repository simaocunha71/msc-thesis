```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```
This function takes an array and a position `k` as input, and returns a new array where the elements from the start of the array up to the position `k` are reversed. The remaining elements in the array are left unchanged. The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function works correctly. 

The function uses Python's list slicing feature to extract the sublist of elements up to position `k`, and then reverses this sublist using slicing with a step of -1. The remaining elements in the array are concatenated with the reversed sublist to form the final result. 

For example, if `arr = [1, 2, 3, 4, 5, 6]` and `k = 4`, the function returns `[4, 3, 2, 1, 5, 6]`, which is the original array with the elements up to position 4 reversed. 

The time complexity of this function is O(n), where n is the length of the input array, because it involves a constant amount of work for each element in the array. The space complexity is O(1), because it only uses a constant amount of additional space to store the result. 