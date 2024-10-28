    numbers.sort()
    min_diff = float('inf')
    result = ()

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i - 1], numbers[i])

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

## Python

```python
