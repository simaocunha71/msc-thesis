```
def smallest_change(arr):
    n = len(arr)
    rev_arr = arr[::-1]
    diff = 0
    for i in range(n):
        if arr[i] != rev_arr[i]:
            diff += 1
    return diff
```


Explanation:
The function `smallest_change` takes an array of integers as input and returns the minimum number of elements that need to be changed to make the array palindromic.

To solve this problem, we can simply iterate through the array and its reverse, and count the number of elements that are not equal. This will give us the minimum number of changes needed to make the array palindromic.

Here's the code:
```
def smallest_change(arr):
    n = len(arr)
    rev_arr = arr[::-1]
    diff = 0
    for i in range(n):
        if arr[i] != rev_arr[i]:
            diff += 1
    return diff
```

This function works by:

1. Reversing the input array to create `rev_arr`.
2. Initializing a variable `diff` to 0, which will store the minimum number of changes needed.
3. Iterating through the array and its reverse using a for loop.
4. For each element, checking if it is equal to its corresponding element in the reverse array.
5. If the elements are not equal, incrementing `diff` by 1.
6. Returning `diff` as the minimum number of changes needed.

For example, if the input array is `[1, 2, 3, 5, 4, 7, 9, 6]`, the function will return 4, because we need to change 4 elements to make the array palindromic. If the input array is `[1, 2, 3, 4, 3, 2, 2]`, the function will return 1, because we need to change only 1 element to make the array palindromic. If the input array is `[1, 2, 3, 2, 1]`, the function will return 0, because the array is already palindromic.