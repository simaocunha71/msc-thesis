Here is a Python function that calculates the sum of the fourth powers of the first n odd natural numbers:

```python
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum
```

In this function, we use a for loop to iterate through the first n odd numbers. The `range(1, 2*n, 2)` generates a sequence of numbers starting from 1, incrementing by 2 until it reaches 2*n (exclusive). This ensures that only odd numbers are included in the iteration.

For each odd number `i`, we calculate its fourth power using `i**4` and add it to the `sum` variable. Finally, we return the total sum.

To test the function with the given assertion, you can use the following code:

```python
print(odd_num_sum(2) == 82)  # This will print True
```

The function will return True if the sum of the fourth powers of the first 2 odd natural numbers is equal to 82, as expected.

```python
def odd_num_sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**4
    return sum
```

This function will calculate the sum of the fourth powers of the first n odd natural numbers. The `range(1, 2*n, 2)` ensures that only odd numbers are included in the iteration. The function then adds the fourth power of each odd number to the `sum` variable and returns the total sum.

To test the function with the assertion `odd_num_sum(2) == 82`, you can use the following code:

```python
print(odd_num_sum(2) == 82)  # This will print True
```

The function will return True if the sum of the fourth powers of the first 2 odd natural numbers is equal to 82, as expected.

```python
def odd_num_sum(n):
    sum = 0
    for i in range(1, 