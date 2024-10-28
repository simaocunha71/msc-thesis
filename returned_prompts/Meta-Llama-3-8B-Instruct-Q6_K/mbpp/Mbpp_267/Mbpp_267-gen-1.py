The problem is asking for a function that takes an integer n and returns the sum of the squares of the first n odd natural numbers. 

The unit test `assert square_Sum(2) == 10` helps clarify the problem by showing that the function should return the sum of the squares of the first n odd natural numbers. 

Here is a python function that solves the problem:
```
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```
This function uses a generator expression to generate the squares of the first n odd natural numbers, and then sums them up using the built-in `sum` function. The `range` function is used to generate the sequence of odd numbers, starting from 1 and ending at 2*n. The step size is 2, which means that the function will generate every other number starting from 1, effectively skipping the even numbers. 

For example, if n is 2, the function will generate the squares of 1 and 3, which are 1 and 9, and then sum them up to get 10. If n is 3, the function will generate the squares of 1, 3, and 5, which are 1, 9, and 25, and then sum them up to get 35. And so on. 