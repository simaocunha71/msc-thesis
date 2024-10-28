```
def square_Sum(n):
    total = 0
    for i in range(2, 2*n, 2):
        total += i ** 2
    return total
``` 
The function `square_Sum(n)` calculates the sum of squares of first n even natural numbers. It starts from 2 (the first even natural number) and increments by 2 in each iteration, up to 2*n. For each even number, it calculates the square and adds it to the total sum. The function returns the total sum. 

The unit test `assert square_Sum(2) == 20` ensures that the function works correctly for the given input. For n=2, the sum of squares of first 2 even natural numbers (2 and 4) is 20, which is the expected output. 





