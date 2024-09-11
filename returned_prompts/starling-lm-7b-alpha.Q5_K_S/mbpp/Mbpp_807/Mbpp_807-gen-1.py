Here's one way to do it:

```python
def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
```

This function will return the first odd number in the list. If none of the numbers in the list are odd, it will return `None`.

Here's an example of how you can use this function:

```python
print(first_odd([1,3,5]))  # prints: 1
print(first_odd([2,4,6]))  # prints: None
```

In the `first_odd` function, we use a `for` loop to go through each number in the list. We use the `%` operator to check if the number is odd (i.e., if the remainder of the division of the number by 2 is not zero). If the number is odd, we immediately return the number, stopping the function and returning the result. If none of the numbers in the list are odd, the function will reach the end of the `for` loop without finding an odd number, and will return `None`.

Note that this function assumes that the input list is non-empty. If you want to handle the case where the list might be empty, you can add a check at the beginning of the function to return `None` if the list is empty.

```python
def first_odd(numbers):
    if not numbers:
        return None
    for n in numbers:
        if n % 2 != 0:
            return n
```

This version of the function will return `None` if the input list is empty, in addition to if none of the numbers are odd.

```python
print(first_odd([]))  # prints: None
```

Here's an example of how you can use this version of the function:

```python
print(first_odd([1,3,5]))  # prints: 1
print(first_odd([]))  # prints: None
```

In the `first_odd` function, we use the `not` operator to check if the list is empty (i.e., if the length of the list is zero). If the list is empty, we