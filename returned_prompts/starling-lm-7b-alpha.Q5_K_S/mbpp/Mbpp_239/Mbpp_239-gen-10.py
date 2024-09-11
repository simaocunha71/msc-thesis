```
def get_total_number_of_sequences(m, n):
    """
    Returns the total number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    >>> get_total_number_of_sequences(10, 4)
    4
    """
    # Initialize the result
    result = 0
    # Initialize the first element of the sequence
    element = 2

    # Compute the total number of possible sequences of length n
    for _ in range(n):
        # If the element is less than or equal to m, increment the result and update the element
        if element <= m:
            result += 1
            element += 1
        # Otherwise, update the element to twice the previous element
        else:
            element *= 2

    return result
```

Here's an example usage of the function:
```python
print(get_total_number_of_sequences(10, 4))  # Output: 4
```

Explanation:
The function `get_total_number_of_sequences` takes in two positive integers `m` and `n` as input. It initializes the result and the first element of the sequence, `element`, to 2. 

Then, it uses a loop to compute the total number of possible sequences of length `n`. In each iteration, if the `element` is less than or equal to `m`, it increments the result by 1 and updates the `element` to be one more than the previous value. If the `element` is greater than `m`, it updates the `element` to be twice the previous value. 

Finally, it returns the result, which is the total number of possible sequences of length `n` that satisfy the given conditions.

In the provided example usage, `get_total_number_of_sequences(10, 4)` is called, which means we are looking for the total number of possible sequences of length 4 where each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to 10. The function returns 4, which is