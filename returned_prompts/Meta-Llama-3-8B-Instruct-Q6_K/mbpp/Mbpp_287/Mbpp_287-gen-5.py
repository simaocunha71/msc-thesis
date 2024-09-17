```
def square_Sum(n):
    return sum(i ** 2 for i in range(2, 2 * n + 1, 2))
```


This function uses a generator expression to calculate the sum of squares of first n even natural numbers. The range function is used to generate the even numbers from 2 to 2n, and the sum function is used to calculate the sum of squares of these numbers. The unit test `assert square_Sum(2) == 20` helps to ensure the correctness of the function. 