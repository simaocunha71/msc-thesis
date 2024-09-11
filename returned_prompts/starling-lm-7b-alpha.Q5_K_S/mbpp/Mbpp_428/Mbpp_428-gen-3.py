Here's one way to implement shell sort in Python:

```python
def shell_sort(arr):
    # Initialize gap
    gap = len(arr) // 2
    while gap > 0:
        # Iterate over the array
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # Swap the elements if required
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # Reduce gap
        gap //= 2
    return arr
```

You can use the function `shell_sort` to sort the given array `[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]`. It will return the sorted array `[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]`.

```python
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```

This assertion will pass if the function `shell_sort` correctly sorts the given array using the shell sort algorithm.

```python
shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
```

This will return `[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]`, which is the sorted version of the input array using shell sort.

```python
print(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 