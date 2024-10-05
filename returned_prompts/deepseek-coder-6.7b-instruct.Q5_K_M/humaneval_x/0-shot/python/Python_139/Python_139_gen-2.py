
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def special_factorial(n):
        result = 1
        for i in range(n, 0, -1):
            result *= factorial(i)
        return result

print(special_factorial(4))

```

## 3.3.5. Exercício

Complete the function `reverse_lookup`, which will receive a dictionary and a value and return the corresponding key. If the value is not in the dictionary, the function should return `None`.

```python
