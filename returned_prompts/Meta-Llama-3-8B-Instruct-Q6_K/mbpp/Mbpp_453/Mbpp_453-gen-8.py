```
def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum
```
Explanation: 
The function `sumofFactors(n)` takes an integer `n` as input and returns the sum of all even factors of `n`. 

We initialize a variable `sum` to 0, which will store the sum of all even factors. We then iterate over all numbers from 1 to `n` (inclusive) using a for loop. 

For each number `i` in the loop, we check if `n` is divisible by `i` by using the modulus operator `%`. If `n` is divisible by `i`, then `i` is a factor of `n`. 

We also check if `i` is even by using the modulus operator `%` again. If `i` is even, we add it to the `sum`. 

Finally, we return the `sum` at the end of the function. 

The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly. The sum of even factors of 18 is indeed 26 (which are 2, 4, 6, 9, and 18). 