```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```


Explanation:
This function takes an array and a position k as input. It returns a new array where the elements up to position k are reversed and the rest of the array remains the same. The slice operation `arr[:k]` gives the elements up to position k and the slice operation `[::-1]` reverses the elements. The remaining elements are obtained by `arr[k:]`. The '+' operator is used to concatenate the two parts. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function works correctly. 

Note: The function returns a new array and does not modify the original array.  If you want to modify the original array, you can use the `arr[:k] = arr[:k][::-1]` statement.  However, this will not pass the unit test as it will modify the original array.  The function is designed to return a new array to avoid modifying the original array.  



For example, if you call `reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)`, the function will return `[4, 3, 2, 1, 5, 6]`. The elements up to position 4 (index 3) are reversed and the rest of the array remains the same.  If you call `reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],6)`, the function will return the original array because there is no need to reverse anything.  If you call `reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],0)`, the function will also return the original array because reversing the entire array is equivalent to not reversing anything.  



The time complexity of this function is O(n) where n is the length of the array. This is because it needs to iterate over the array once to reverse the elements up to position k. The space complexity is also O(n) because it needs to create a new array to store the result.  



This function is useful when you need to reverse a part