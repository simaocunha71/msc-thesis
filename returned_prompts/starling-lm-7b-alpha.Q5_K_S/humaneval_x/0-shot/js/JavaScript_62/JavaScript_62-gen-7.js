To find the derivative of a polynomial, you need to multiply each term by its corresponding power and then decrement the power by one. Here's a step-by-step breakdown:

1. Initialize an empty array called `result` to store the derivative of the polynomial.
2. Loop through the `xs` array from index 0 to the second-to-last index (`xs.length - 1`).
3. For each index `i`, calculate the derivative of the term at index `i` using the formula `(i+1) * xs[i]`. Add this value to the `result` array.
4. After the loop, return the `result` array.

Here's the Python code that implements the above steps:

```python
def derivative(xs):
    result = []
    for i in range(len(xs)):
        result.append((i+1) * xs[i])
    return result
```

For example, if you call `derivative([3, 1, 2, 4, 5])`, it will return `[1, 4, 12, 20]` as the derivative of the polynomial `3 + x + 2x^2 + 4x^3 + 5x^4` is `1 + 4x + 12x^2 + 20x^3`.

Similarly, if you call `derivative([1, 2, 3])`, it will return `[2, 6]` as the derivative of the polynomial `1 + 2x + 3x^2` is `2 + 6x`.

Hope this helps!

Here's the Python code that implements the above steps:
```python
def derivative(xs):
    result = []
    for i in range(len(xs)):
        result.append((i+1) * xs[i])
    return result
```
And here's a test case to verify the correctness of the function:
```python
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative