```
def cube_Sum(n):
    return sum(i**3 for i in range(2, 2*n+1, 2))
```


The function takes an integer n as input and returns the sum of the cubes of the first n even natural numbers. The unit test `assert cube_Sum(2) == 72` helps to understand the problem better. It indicates that the function should return 72 when the input is 2, which is the sum of the cubes of the first 2 even natural numbers (2^3 and 4^3).

The solution uses a generator expression inside the built-in sum function to calculate the sum of the cubes of the first n even natural numbers. The range function is used to generate the sequence of even numbers, starting from 2, up to 2n, incrementing by 2 each time. The result is the sum of the cubes of these numbers.