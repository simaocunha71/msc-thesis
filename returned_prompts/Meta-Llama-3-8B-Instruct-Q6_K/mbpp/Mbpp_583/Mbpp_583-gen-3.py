```
def catalan_number(n):
    if n <= 1:
        return 1
    catalan = [0]*(n+1)
    catalan[0] = catalan[1] = 1
    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-1-j]
    return catalan[n]
```    
The function `catalan_number` calculates the nth Catalan number using dynamic programming. It first checks if `n` is less than or equal to 1, in which case it returns 1. Then it initializes a list `catalan` of size `n+1` and sets the first two elements to 1. It then calculates the Catalan numbers from the third element onwards using the formula `catalan[i] = sum(catalan[j] * catalan[i-1-j] for j in range(i))`. Finally, it returns the `n`th Catalan number.

The unit test `assert catalan_number(10)==16796` ensures that the function returns the correct value for the 10th Catalan number.