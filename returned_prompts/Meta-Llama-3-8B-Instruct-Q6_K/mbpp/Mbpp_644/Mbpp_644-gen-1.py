```
def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]
```


Explanation:
The function `reverse_Array_Upto_K` takes two arguments: an array `arr` and an integer `k`. It returns a new array where the elements up to position `k` are reversed and the rest of the array remains the same.

We use list slicing to get the elements up to position `k` (`arr[:k]`) and then reverse this slice (`[::-1]`). We then concatenate this reversed slice with the rest of the array (`arr[k:]`) to get the final result. 

The unit test `assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]` ensures that the function works correctly. 

For example, if the input array is `[1, 2, 3, 4, 5, 6]` and `k` is `4`, the function should return `[4, 3, 2, 1, 5, 6]`. This is because the elements up to position `4` (`[1, 2, 3, 4]`) are reversed to `[4, 3, 2, 1]` and the rest of the array (`[5, 6]`) remains the same. 





# Python code to reverse an array up to a given position
def reverse_Array_Upto_K(arr, k):
    # reverse the array up to position k
    return arr[:k][::-1] + arr[k:]

# test the function
arr = [1, 2, 3, 4, 5, 6]
k = 4
print(reverse_Array_Upto_K(arr, k))  # Output: [4, 3, 2, 1, 5, 6]

```

Output:
```
[4, 3, 2, 1, 5, 6]
```



# Python code to reverse an array up to a given position
def reverse_Array_Upto_K(arr, k):
    # reverse the array up to position k
    return arr[:k][::-1] + arr[k:]

# test the function
arr = [1, 2, 3, 4, 5,