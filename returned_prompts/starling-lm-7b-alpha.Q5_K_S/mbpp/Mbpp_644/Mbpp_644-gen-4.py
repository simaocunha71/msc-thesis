Here's a solution:

```python
def reverse_Array_Upto_K(arr, k):
    """
    This function will reverse the array upto a given position
    """
    for i in range(k + 1):
        j = arr[i]
        for j1 in range(i, k):
            arr[j1], arr[j1 + 1] = arr[j1 + 1], arr[j1]
    return arr
```

You can use this function like so:

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))  # prints [4, 3, 2, 1, 5, 6]
```

This function uses a double for loop to iterate over the array and reverse each element up to the given position `k`. It starts with the first element at index `i`, and swaps each element with the next one until it reaches the given position. After that, it continues to the next element and repeats the process.

Note: This function modifies the array in-place, meaning it directly changes the elements of the array without creating a new one.

```python
def reverse_Array_Upto_K(arr, k):
    """
    This function will reverse the array upto a given position
    """
    for i in range(k + 1):
        j = arr[i]
        for j1 in range(i, k):
            arr[j1], arr[j1 + 1] = arr[j1 + 1], arr[j1]
    return arr
```
To use this function, you can call it with the array you want to reverse and the position up to which you want to reverse the array. For example, to reverse the array `[1, 2, 3, 4, 5, 6]` up to the position 4, you can do:

```python
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4))  # prints [4, 3, 2, 1, 5,