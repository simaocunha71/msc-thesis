Here's a Python function that calculates the sum of the fourth power of the first n odd natural numbers:

```python
def odd_num_sum(n):
    sum_of_fourth_power = 0
    for i in range(1, 2 * n + 1, 2):
        sum_of_fourth_power += i ** 4
    return sum_of_fourth_power
```

This function uses a for loop to iterate through the odd numbers from 1 to 2 * n (inclusive) in steps of 2. For each odd number, it calculates its fourth power and adds it to the sum_of_fourth_power variable. Finally, it returns the total sum.

To test the function, you can use the assert statement like this:

```python
assert odd_num_sum(2) == 82
```

This assertion checks if the function returns 82 when n is 2, as expected. If the function returns a different value, an AssertionError will be raised, indicating that the function is not working correctly.

The time complexity of this function is O(n), as it iterates through n odd numbers.

```python
def odd_num_sum(n):
    sum_of_fourth_power = 0
    for i in range(1, 2 * n + 1, 2):
        sum_of_fourth_power += i ** 4
    return sum_of_fourth_power
```

```python
assert odd_num_sum(2) == 82
```

By using this function and the assert statement, you can easily calculate the sum of the fourth power of the first n odd natural numbers in Python.

```python
def odd_num_sum(n):
    sum_of_fourth_power = 0
    for i in range(1, 2 * n + 1, 2):
        sum_of_fourth_power += i ** 4
    return sum_of_fourth_power
```

```python
assert odd_num_sum(2) == 82
```

By utilizing this Python function and the