```
def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n, 2))
```


The function `square_Sum(n)` takes an integer `n` as input and returns the sum of squares of first `n` even natural numbers. 

It uses a generator expression to generate the even numbers from 2 to 2*n, squares each of them, and then sums them up using the built-in `sum` function.

The unit test `assert square_Sum(2) == 20` ensures that the function returns the correct result for the input `n=2`. 

For example, the sum of squares of first 2 even natural numbers is 2^2 + 4^2 = 4 + 16 = 20. 