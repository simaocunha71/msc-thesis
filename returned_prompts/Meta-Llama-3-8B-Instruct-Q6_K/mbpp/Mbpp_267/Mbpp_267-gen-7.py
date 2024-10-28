```
def square_Sum(n):
    return sum(i ** 2 for i in range(1, 2 * n, 2))
```
This function uses a generator expression to generate the squares of the first n odd natural numbers and then sums them up using the built-in sum function. The range function is used to generate the sequence of odd numbers, starting from 1 and ending at 2n-1. The step size is 2, which means we skip every even number and only include the odd numbers in the sequence. 

For example, if n is 2, the function will generate the sequence 1, 3 and then square them to get 1 and 9, and finally sum them up to get 10. This is confirmed by the unit test `assert square_Sum(2) == 10`. 

This function has a time complexity of O(n) because it needs to iterate over the sequence of n odd numbers. The space complexity is O(1) because it only uses a constant amount of space to store the sum and the generator expression. 