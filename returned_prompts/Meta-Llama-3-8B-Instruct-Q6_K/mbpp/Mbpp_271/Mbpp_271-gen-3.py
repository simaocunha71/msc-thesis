```
def even_Power_Sum(n):
    return sum([i**5 for i in range(2, 2*n, 2)])
```





The function takes an integer `n` as input and returns the sum of the first `n` even natural numbers raised to the fifth power. The unit test `assert even_Power_Sum(2) == 1056` helps to clarify the problem by showing that the function should return the sum of the squares of the first 2 even numbers, which is `2^5 + 4^5 = 32 + 1024 = 1056`. 

The function uses a list comprehension to generate the squares of the first `n` even natural numbers, and the built-in `sum` function to calculate their sum. The `range` function is used to generate the sequence of even numbers, starting from 2 and incrementing by 2 each time. The `**` operator is used to raise each number to the fifth power.