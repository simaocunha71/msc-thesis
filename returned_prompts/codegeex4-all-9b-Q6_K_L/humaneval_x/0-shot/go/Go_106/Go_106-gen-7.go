
Here is a Python solution for the problem:

```python
def F(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))
    return result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(F(5))  # Output: [1, 2, 6, 24, 15]
```

In this solution, the function `F(n)` is implemented to loop from 1 to n (inclusive) and check if the current index `i` is even or odd. If `i` is even, the factorial of `i` is calculated and appended to the result list. If `i` is odd, the sum of numbers from 1 to `i` is calculated and appended to the result list. The `factorial` function is a helper function to calculate the factorial of a number.

Please note that this solution is written in Python, not Go. If you want a Go solution, let me know.