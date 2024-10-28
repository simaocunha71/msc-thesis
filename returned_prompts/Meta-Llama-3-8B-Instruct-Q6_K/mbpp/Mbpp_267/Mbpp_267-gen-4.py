```
def square_Sum(n):
    return sum([i**2 for i in range(1, 2*n, 2)])
```


The function takes an integer `n` as input and returns the sum of the squares of the first `n` odd natural numbers. The function uses list comprehension to generate the list of squares of the first `n` odd natural numbers and then calculates the sum of these squares.

The unit test `assert square_Sum(2) == 10` ensures that the function works correctly for the input `n=2`. This test case is used to verify that the function returns the correct result for the sum of the squares of the first two odd natural numbers, which is `1^2 + 3^2 = 10`. 

This function can be used to calculate the sum of the squares of the first `n` odd natural numbers for any positive integer `n`. It is an efficient and concise solution that uses list comprehension to generate the list of squares and the built-in `sum` function to calculate the sum. 