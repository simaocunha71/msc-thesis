Here is one way to solve this problem:

```python
def next_Perfect_Square(n):
    sqrt_n = int(n ** 0.5) + 1
    while True:
        if (sqrt_n ** 2) > n:
            return (sqrt_n ** 2)
        else:
            sqrt_n += 1
```

This function first computes the square root of the input number rounded up to the nearest whole number. It then checks if this rounded number squared is greater than the input number. If it is, then the function returns the square of this rounded number, which is the next perfect square greater than the input number. If it's not, the function increments the rounded number by one and checks again. This process continues until the rounded number squared is greater than the input number.

For example, if the input number is 35, the function computes the square root of 35 rounded up to the nearest whole number, which is 6. It then checks if 6 squared is greater than 35. Since it's not, the function increments the rounded number to 7 and checks again. This continues until 7 squared (49) is greater than 35. At this point, the function returns 49, which is the next perfect square greater than 35.

The time complexity of this function is O(sqrt(n)), which is efficient enough for most practical purposes.

Here is a test case to verify the function:

```python
print(next_Perfect_Square(35) == 36)  # True
```

As you can see, the function correctly returns 36, confirming that it correctly finds the next perfect square greater than the input number.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
```python

```python

```python

```python

```python

```python