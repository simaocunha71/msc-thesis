Here's one way to do it:

```python
def max_Abs_Diff(A):
    max_diff = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            diff = abs(A[i] - A[j])
            max_diff = max(max_diff, diff)
    return max_diff
```

The function `max_Abs_Diff` takes a list `A` as input and initializes the `max_diff` variable to 0. It then uses two nested loops to compare every pair of elements in the list. For each pair, it calculates the absolute difference using the `abs()` function and updates the `max_diff` variable if a larger difference is found. Finally, it returns the maximum difference found.

To test the function, you can use the `assert` statement to verify that the function correctly calculates the maximum absolute difference for a given input array. In the example provided, `max_Abs_Diff((2,1,5,3))` should return 4, as the maximum absolute difference between any two elements in the array (2, 1, 5, 3) is 4.

```python
assert max_Abs_Diff((2,1,5,3)) == 4
```

This assertion will raise an `AssertionError` if the function does not return the expected result, indicating that there is an error in the implementation of `max_Abs_Diff`.

```python
def max_Abs_Diff(A):
    max_diff = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            diff = abs(A[i] - A[j])
            max_diff = max(max_diff, diff)
    return max_diff

assert max_Abs_Diff((2,1,5,3)) == 4
```

This code will pass the assertion and execute without raising an error, indicating that the `max_Abs_Diff` function correctly calculates the maximum absolute difference between any two elements in a given array.

```python
def max_Abs_Diff(A):
    max_diff =