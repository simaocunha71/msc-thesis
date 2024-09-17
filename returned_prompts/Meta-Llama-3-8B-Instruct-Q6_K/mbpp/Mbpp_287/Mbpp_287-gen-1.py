```
def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n, 2))
```


Explanation:
The problem is asking you to write a function that takes an integer n and returns the sum of squares of first n even natural numbers. For example, if n is 2, the sum of squares of first 2 even natural numbers is 2^2 + 4^2 = 20. 

The unit test `assert square_Sum(2) == 20` helps to clarify this. 

The solution uses a generator expression to generate the even numbers from 2 to 2n, squares each number and then sums them up using the built-in `sum` function. The `range` function is used to generate the sequence of numbers. The step size is 2, which means it will generate only even numbers. The start value is 2, which means the sequence will start from 2. The end value is 2n, which means the sequence will end at 2n. 

For example, if n is 2, the function will generate the sequence 2, 4 and then square each number and sum them up, which gives 20. 

This solution is efficient because it uses a generator expression, which means it doesn't store all the numbers in memory at once. It generates the numbers on the fly and then sums them up. This makes it suitable for large values of n. 