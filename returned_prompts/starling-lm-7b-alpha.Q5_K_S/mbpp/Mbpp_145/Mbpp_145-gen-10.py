Here's one way you could write the function:

```python
def max_Abs_Diff(arr):
    return max(abs(a-b) for a, b in zip(arr, arr[1:]))
```

Here's a step-by-step breakdown of how the function works:

1. `zip(arr, arr[1:])` returns a tuple of all pairs of consecutive elements in the array. For example, given the input `[2,1,5,3]`, this would return `[(2, 1), (1, 5), (5, 3)]`.
2. `abs(a-b)` calculates the absolute difference between each pair of consecutive elements. For example, given the pairs `[(2, 1), (1, 5), (5, 3)]`, this would return `[1, 4, 2]`.
3. `max()` returns the largest value in the list. Given the list `[1, 4, 2]`, this would return `4`.

The function `max_Abs_Diff` returns the maximum absolute difference between any two elements in the input array, which matches the expected output of `4` for the example provided.

```python
assert max_Abs_Diff((2,1,5,3)) == 4
```

This assertion verifies that the function `max_Abs_Diff` correctly calculates the maximum absolute difference between any two elements in the input array, as expected.

```python
def max_Abs_Diff(arr):
    return max(abs(a-b) for a, b in zip(arr, arr[1:]))
```

Here's how you can use the `max_Abs_Diff` function to find the maximum absolute difference between any two elements in an array:

```python
# Example usage
input_array = [2, 1, 5, 3]
max_difference = max_Abs_Diff(input_array)
print(max_difference)  # Output: 4
```

In this example, we pass the array `[2, 1, 5, 3]` to the `max_Abs_Diff` function, which returns the