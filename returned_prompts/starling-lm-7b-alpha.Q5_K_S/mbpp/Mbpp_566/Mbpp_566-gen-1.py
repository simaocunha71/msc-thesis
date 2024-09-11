def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

```

```
def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum
```


Explanation:
The function `sum_digits(n)` takes an integer `n` as an argument and returns the sum of its digits. 

The function uses a while loop to iterate through the digits of the number. Inside the loop, it adds the last digit of `n` (obtained using the modulus operator `%`) to the sum variable, and then updates `n` by removing the last digit (using the floor division operator `//`). This process continues until `n` becomes 0, which means all digits have been processed.

Finally, the function returns the sum of the digits.

In the provided example, the function is tested with the input `345`, and the expected output is `12`. This means that the sum of the digits in `345` is indeed `12`.
```

```python
def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum
```

The above code defines a function `sum_digits(n)` that calculates the sum of the digits of a non-negative integer `n`. The function uses a while loop to iterate through the digits of `n`. Inside the loop, it adds the last digit of `n` (obtained using the modulus operator `%`) to the `sum` variable, and then updates `n` by removing the last digit (using the floor division operator `//`). This process continues until `n` becomes 0, which means all digits have been processed.

Finally, the function returns the sum of the digits.

In the provided example, the function is tested with the input `345`, and the expected output is `12`. This means that the sum of the dig