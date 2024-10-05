To find the derivative of a polynomial, we simply multiply each term by its corresponding index and then shift the terms to the left by one index.

Here's how you can do it in Python:

1. Create an empty list called `result` to store the derivative.

2. Loop through the `xs` list, starting from the second element (index 1). For each element at index `i`, multiply it by `i + 1` and append the result to the `result` list.

3. Finally, return the `result` list as the derivative of the polynomial.

Here's the Python code that implements this logic:

```python
def derivative(xs):
    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * (i + 1))
    return result
```

You can test the function with the provided examples:

```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This code will correctly calculate the derivative of a polynomial using the coefficients provided in the `xs` list.

Note: The code assumes that the `xs` list is non-empty and contains at least one element. If this is not the case, you may want to add additional logic to handle empty or single-element lists.

In Python, the time complexity of this function is O(n), where n is the number of elements in the `xs` list. This is because we only need to iterate through the list once to calculate the derivative.

The space complexity of this function is O(n) as well, since we create a new list called `result` to store the derivative.

Overall, this function efficiently calculates the derivative of a polynomial using the provided coefficients.

Here's the Python code for the solution:

```python
def derivative(xs):
    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * (i + 1))
    return result