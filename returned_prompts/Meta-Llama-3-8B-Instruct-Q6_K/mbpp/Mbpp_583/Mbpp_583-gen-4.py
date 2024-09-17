```
def catalan_number(n):
    if n <= 1:
        return 1
    else:
        catalan = [1]*(n+1)
        for i in range(2, n+1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i-j-1]
        return catalan[n]
```        
The problem is to write a function that returns the nth Catalan number. The function should be able to calculate the nth Catalan number efficiently.

The provided unit test `assert catalan_number(10)==16796` suggests that the function should be able to calculate the 10th Catalan number, which is 16796.

Here is the solution in Python:
```
def catalan_number(n):
    if n <= 1:
        return 1
    else:
        catalan = [1]*(n+1)
        for i in range(2, n+1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i-j-1]
        return catalan[n]
```
This function uses dynamic programming to calculate the nth Catalan number. It initializes a list `catalan` with the first `n+1` elements as 1, and then iterates from 2 to `n+1` to calculate the Catalan numbers. For each `i` from 2 to `n+1`, it calculates the `i`th Catalan number as the sum of the product of the `j`th Catalan number and the `(i-j-1)`th Catalan number for all `j` from 0 to `i-1`. Finally, it returns the `n`th Catalan number.

This function has a time complexity of O(n^2) and a space complexity of O(n), making it efficient for calculating large Catalan numbers.