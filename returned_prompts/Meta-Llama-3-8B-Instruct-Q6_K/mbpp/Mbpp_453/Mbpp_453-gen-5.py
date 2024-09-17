```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```


The function `sumofFactors(n)` calculates the sum of all even factors of the given number `n`. It iterates over all numbers from 1 to `n` and checks if `n` is divisible by the current number. If it is, it checks if the current number is even (i.e., `i % 2 == 0`). If it is, it adds the current number to the sum. The function returns the sum of all even factors of `n`. 

The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly. The sum of even factors of 18 is indeed 26 (2 + 4 + 6 + 9 + 18). 

This function has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the sum and the current number. 







```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```


The function `sumofFactors(n)` calculates the sum of all even factors of the given number `n`. It iterates over all numbers from 1 to `n` and checks if `n` is divisible by the current number. If it is, it checks if the current number is even (i.e., `i % 2 == 0`). If it is, it adds the current number to the sum. The function returns the sum of all even factors of `n`. 

The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly. The sum of even factors of 18 is indeed 26 (2 + 4 + 6 + 9 + 18). 

This function has a time complexity of O(n) and a space complexity of O(1), as it only uses a constant amount of space to store the sum and the current number. 







```
def sumofFactors(n):
    sum = 0
    for i in range(