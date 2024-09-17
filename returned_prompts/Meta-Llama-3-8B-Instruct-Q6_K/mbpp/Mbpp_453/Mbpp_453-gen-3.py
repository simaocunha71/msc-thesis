```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum
```


In this function, we are iterating over all numbers from 1 to n (inclusive). For each number, we check if it is a factor of n (i.e., n % i == 0) and if it is even (i % 2 == 0). If both conditions are met, we add it to the sum. Finally, we return the sum.

The unit test `assert sumofFactors(18) == 26` ensures that the function is working correctly. For example, the even factors of 18 are 2, 6, 9, and 18, and their sum is 35, but the problem asks for the sum of the even factors, which is 26. Therefore, the function is correctly implemented.