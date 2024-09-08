Here is a Python solution using the binomial theorem:

```python
def binomial(n):
    return n * (n-1) // 2

def sum_Of_product(n):
    sum_ = 0
    for i in range(1, n):
        sum_ += binomial(i) * binomial(i+1)
    return sum_

print(sum_Of_product(3))  # 15
```

In the given code, we first define a helper function `binomial` that calculates the binomial