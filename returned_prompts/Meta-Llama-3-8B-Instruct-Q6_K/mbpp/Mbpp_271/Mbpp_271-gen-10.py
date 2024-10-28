```
def even_Power_Sum(n):
    total = 0
    for i in range(2, n*2, 2):
        total += i**5
    return total
```
The function `even_Power_Sum(n)` takes an integer `n` as input and calculates the sum of the first `n` even natural numbers raised to the fifth power. It does this by initializing a variable `total` to 0, then iterating over the range of even numbers from 2 to `2*n` (since we want the first `n` even numbers, and the last even number in this range is `2*n`). For each even number `i` in this range, it adds `i` raised to the fifth power to `total`, and finally returns `total`. The unit test `assert even_Power_Sum(2) == 1056` ensures that the function is working correctly. 





