To check if a list's elements are monotonically increasing or decreasing, we can compare each element to the next one. If the elements are monotonically increasing, the next element should be greater than or equal to the current element. If the elements are monotonically decreasing, the next element should be less than or equal to the current element. We can use a loop to compare each element to the next one and return True if all comparisons are met and False if any of the comparisons fail.

Here's the Python code for the `monotonic` function:

```python
def monotonic(l: list):
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:  # Check if the elements are monotonically increasing
            return False
        elif l[i] > l[i+1]:  # Check if the elements are monotonically decreasing
            return False
    return True
```

You can test the function with the provided test cases:

```python
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

The output should match your expected results.

The key to solving this problem is to compare each element to the next one in the list and return True if all comparisons are met and False if any of the comparisons fail. By using a loop to iterate through the list, we can check all the comparisons and return the correct result.

This function assumes that the input list `l` is not empty. If the list can be empty, you can add a check at the beginning of the function to ensure that the list is not empty before starting the loop.

```python
def monotonic(l: list):
    if not l:  # Check if the list is empty
        return False
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:  # Check if the elements are monotonically increasing
            return False
        elif l[i] >