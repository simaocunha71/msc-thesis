```
def next_Perfect_Square(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1
```



In this problem, we need to find the next perfect square greater than a given number. We can solve this problem by iterating through perfect squares until we find one that is greater than the given number.

Here's how we can implement it in Python:

```python
def next_Perfect_Square(n):
    i = 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1
```

The unit test `assert next_Perfect_Square(35) == 36` helps to clarify the expected output. It shows that the function should return the next perfect square after the given number, which in this case is 36.

The function works by starting with the smallest perfect square (1) and iterating through the sequence of perfect squares until it finds one that is greater than the given number. The first perfect square that meets this condition is returned as the result.