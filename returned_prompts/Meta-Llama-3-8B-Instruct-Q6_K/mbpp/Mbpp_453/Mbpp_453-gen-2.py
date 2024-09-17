```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```


The function `sumofFactors(n)` takes an integer `n` as input and returns the sum of all even factors of `n`. It iterates over all numbers from 1 to `n` (inclusive) and checks if each number is a factor of `n` by using the modulo operator (`%`). If a number is a factor, it checks if the number is even by using the modulo operator again. If the number is even, it adds the number to the sum. Finally, it returns the sum of all even factors.

The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly. The sum of even factors of 18 is 2 + 6 + 9 + 18 = 26.