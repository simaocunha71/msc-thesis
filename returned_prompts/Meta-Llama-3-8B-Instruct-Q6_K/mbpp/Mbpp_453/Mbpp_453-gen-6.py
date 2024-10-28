```
def sumofFactors(n):
    factors = [i for i in range(1, n+1) if n%i == 0]
    return sum([i for i in factors if i % 2 == 0])
```


Explanation:
The function sumofFactors(n) calculates the sum of even factors of a given number n. It does this by first generating a list of all factors of n, and then summing up the even factors in this list.

The unit test `assert sumofFactors(18) == 26` ensures that the function works correctly for the input 18, which has even factors 2, 4, and 6. The sum of these even factors is 12, but the unit test also includes the even factors 1 and 18, which are technically even factors of 18 but are often excluded from the definition of "even factors". The unit test is testing the function with this broader definition of "even factors", so we need to include these extra factors in our code.

The code uses list comprehensions to generate the lists of factors and even factors. It then uses the built-in sum function to calculate the sum of the even factors. The function returns this sum.