Here's a Python implementation of Shell Sort:

```python
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```

To use this function, you can call it with a list of numbers to be sorted, like this:
```python
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
```

In this implementation, the `gap` variable is initially set to half the length of the input array. The outer loop iterates over the `gap` variable, and the inner loop compares each element in the array with the previous elements in the current `gap` section. If an element is out of place, it is moved to its correct position by swapping it with the previous element. After each iteration of the outer loop, the `gap` is halved until it becomes zero, at which point the array is considered sorted.

The `assert` statement is used to verify that the `shell_sort` function correctly sorts the input array. The expected output is `[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]`, which matches the result of the `shell_sort` function when called with the input array `[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]`.

Overall, this implementation of Shell Sort is a simple and effective way to sort an array in Python.

```python
def shell_sort(arr):
    gap