```
def square_Sum(n):
    total = 0
    for i in range(1, 2*n, 2):
        total += i ** 2
    return total
``` 
The function `square_Sum` takes an integer `n` as input and returns the sum of the squares of the first `n` odd natural numbers. It does this by initializing a variable `total` to 0, then iterating over the range from 1 to 2*n with a step of 2 (which gives all odd numbers up to 2*n-1). For each number `i` in this range, it adds `i` squared to `total`. Finally, it returns `total`. This solution passes the given unit test `assert square_Sum(2) == 10`. 

For example, for `n=2`, the function will iterate over the numbers 1, 3, and add their squares (1 and 9) to `total`, resulting in a total of 10. 

Note: The unit test `assert square_Sum(2) == 10` is checking if the function returns the correct sum of squares for the first 2 odd natural numbers (1 and 3), which is 10. This test helps to validate the correctness of the function. 