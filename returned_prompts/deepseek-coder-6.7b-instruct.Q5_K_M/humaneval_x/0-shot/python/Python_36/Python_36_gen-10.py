

def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))


# Alternative solution
def fizz_buzz(n: int) -> int:
    return sum(str(i).count('7') for i in range(n) if i % 11 == 0 or i % 13 == 0)


print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))


# Alternative solution
def fizz_buzz(n: int) -> int:
    return sum(map(lambda x: str(x).count('7'), filter(lambda x: x % 11 == 0 or x % 13 == 0, range(n))))


print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

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
