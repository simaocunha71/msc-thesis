```
def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n, 2))
```
This function uses a generator expression to generate the squares of the first n even natural numbers, and then sums them up using the built-in sum function. The range function is used to generate the sequence of even numbers, starting from 2 and incrementing by 2 each time.

The unit test `assert square_Sum(2) == 20` helps to clarify the problem by specifying the expected output for a given input. In this case, the function should return 20 when given the input 2, which is the sum of the squares of the first 2 even natural numbers: 2^2 + 4^2 = 4 + 16 = 20.