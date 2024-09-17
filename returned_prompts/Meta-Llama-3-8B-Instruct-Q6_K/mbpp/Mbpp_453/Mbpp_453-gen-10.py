```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
``` 
The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly. It checks if the sum of even factors of 18 is 26, which is the expected output. 

The function works by iterating over all numbers from 1 to the input number `n`. For each number, it checks if it is a factor of `n` by checking if `n % i == 0`. If it is a factor, it checks if it is even by checking if `i % 2 == 0`. If it is even, it adds it to the sum. Finally, it returns the sum of even factors. 