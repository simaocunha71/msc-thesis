```
def reverse_Array_Upto_K(arr, k):
    arr = arr[:k][::-1] + arr[k:]
    return arr
```


Explanation:
This function takes two parameters: an array and a position `k`. It reverses the array up to the position `k` and then returns the modified array.

The function uses slicing to get the portion of the array up to position `k` (`arr[:k]`) and then reverses it (`[::-1]`). It then concatenates this reversed portion with the remaining part of the array (`arr[k:]`).

For example, if the input array is `[1, 2, 3, 4, 5, 6]` and `k` is `4`, the function will return `[4, 3, 2, 1, 5, 6]`. This is because the array is reversed up to the position `4`, resulting in `[4, 3, 2, 1]`, and then concatenated with the remaining part of the array (`[5, 6]`).