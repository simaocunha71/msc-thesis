To solve this problem, we can follow these steps:

1. Sort the list in ascending order. This is because the median of a list is the middle value when the list is sorted.
2. If the length of the list is even, the median is the average of the two middle values.
3. If the length of the list is odd, the median is the middle value.

Here's the code to implement this logic:

```python
def median(l: list):
    # Step 1: Sort the list
    l.sort()

    # Step 2: Calculate the median
    n = len(l)
    if n % 2 == 0:  # If the length of the list is even
        # The median is the average of the two middle values
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:  # If the length of the list is odd
        # The median is the middle value
        return l[n // 2]
```

You can test the function with the provided test cases:

```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

These test cases check if the function correctly calculates the median for a list of integers and a list of positive and negative integers.

I hope this helps! Let me know if you have any more questions.

```

```

```python
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Step 1: Sort the list
    l.sort()

    # Step 2: Calculate the median
    n = len(l)
    if n % 2 == 0