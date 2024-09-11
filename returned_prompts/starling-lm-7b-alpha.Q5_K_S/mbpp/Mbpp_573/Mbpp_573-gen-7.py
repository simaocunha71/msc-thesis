def unique_product(lst):
    return reduce(lambda x,y: x*y, set(lst))


"""
The reduce function applies a binary function to the (accumulated) intermediate
results of applications of the function so far, and the initial value.

In this case, reduce(lambda x,y: x*y, set(lst)) calculates the product of all unique numbers in lst.
"""

# Test
print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# To ensure the correctness of the function, we can use the `assert` statement.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000

# If the function is correct, the above `assert` statement will not raise an exception.
# If the function is incorrect, the `assert` statement will raise an exception.

"""
To verify this, we can use the `assert` statement in Python.
The `assert` statement checks if the condition is `True`.
If the condition is `True`, the program continues to execute the next statement.
If the condition is `False`, the program raises an `AssertionError` exception, which stops the program from executing the next statement.
"""
```

```

```

To ensure the correctness of the function, we can use the `assert` statement.

```python
# Test
print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# To ensure the correctness of the function, we can use the `assert` statement.
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
```

If the function is correct, the above `assert