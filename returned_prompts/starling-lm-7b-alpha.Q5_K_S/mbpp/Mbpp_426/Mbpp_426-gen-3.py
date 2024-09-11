```
def filter_oddnumbers(numbers):
    """
    Yields the odd numbers from the given list.
    """
    for number in numbers:
        if number % 2 != 0:
            yield number
```

