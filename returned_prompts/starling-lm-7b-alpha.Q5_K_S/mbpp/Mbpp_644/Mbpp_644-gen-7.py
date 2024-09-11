Here is a Python function to reverse an array upto a given position:

```python
def reverse_Array_Upto_K(arr, k):
    start = 0
    end = len(arr) - 1
    while start < k:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
```

Here is how to use the function:

```python
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
```

This function swaps the elements from start to end of the array, effectively reversing them. It starts at the start position and ends at the end position of the array, swapping each pair of elements. The start position moves towards the end of the array, while the end position moves towards the start of the array.

The function takes two parameters: arr, the array to be reversed, and k, the position up to which the array should be reversed.

The function uses two pointers, start and end, initialized to the start and end of the array respectively. It swaps the elements at these positions using a simultaneous assignment, then moves the pointers towards each other. This process continues until the start pointer is equal to or greater than k.

Finally, the function returns the reversed array.

The assert statement checks if the function returns the expected result for the given input.

```python
def reverse_Array_Upto_K(arr, k):
    start = 0
    end = len(arr) - 1
    while start < k:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
```

This function is a simple and efficient way to reverse an array up to a given position. It has a time complexity of O(n), where n is the size of the array, as it swaps each pair of elements only once.

```python
assert reverse_Array_Upto_K([1, 2, 3,