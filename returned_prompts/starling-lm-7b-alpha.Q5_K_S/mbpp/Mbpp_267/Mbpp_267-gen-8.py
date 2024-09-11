Here is a Python function that takes an integer n and returns the sum of the squares of the first n odd natural numbers:

```python
def square_Sum(n):
    total = 0
    for i in range(1, 2*n+1, 2):
        total += i ** 2
    return total
```

In the above function, we initialize a variable `total` to zero. We use a `for` loop to iterate through the first n odd natural numbers. The `range()` function is used to generate a sequence of numbers from 1 to 2*n+1 with a step of 2. This ensures that we only consider odd numbers. Inside the loop, we square each number `i` and add it to the `total`. Finally, we return the `total`.

To test the function, you can use the `assert` statement to verify if the function returns the correct result for a given input. For example, if you expect the function to return 10 for the input 2, you can write:

```python
assert square_Sum(2) == 10
```

This will raise an error if the function does not return the expected result.

```python
def square_Sum(n):
    total = 0
    for i in range(1, 2*n+1, 2):
        total += i ** 2
    return total
```

This function takes an integer `n` as input and returns the sum of the squares of the first `n` odd natural numbers. The `for` loop iterates through the range of odd numbers from 1 to 2*n+1, squares each number, and accumulates the sum in the `total` variable. Finally, the `total` is returned as the result.

You can test the function by using the `assert` statement to verify if the function returns the correct result for a given input. For example, if you expect the function to return 10 for the input 2, you can write:

```python
assert square_Sum(2) == 10
```

This will raise an error if the function does not return the expected result.

```python
def square_Sum(n):
    total = 