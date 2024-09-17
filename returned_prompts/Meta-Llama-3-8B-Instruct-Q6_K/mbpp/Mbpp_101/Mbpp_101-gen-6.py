```
def kth_element(arr, k):
    if k < 1:
        return "Invalid input"
    return arr[k-1]
```



The function takes two parameters: a list `arr` and an integer `k`. It checks if `k` is less than 1, and if so, returns the string "Invalid input". Otherwise, it returns the element at index `k-1` in the list. This is because 1-based indexing is used, so we need to subtract 1 from `k` to get the correct index. For example, if `k` is 2, the function returns the element at index 1 (since Python uses 0-based indexing). If `k` is 3, the function returns the element at index 2, and so on. The unit test `assert kth_element([12,3,5,7,19], 2) == 3` verifies that the function works correctly.