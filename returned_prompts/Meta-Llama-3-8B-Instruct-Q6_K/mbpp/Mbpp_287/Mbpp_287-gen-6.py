```
def square_Sum(n):
    return sum(i ** 2 for i in range(2, 2 * n + 1, 2))
```


The function square_Sum takes an integer n as input and returns the sum of squares of the first n even natural numbers. The function uses a generator expression to generate the even numbers from 2 to 2n, and then squares each number and sums them up. The unit test `assert square_Sum(2) == 20` ensures that the function works correctly for n = 2. 

For example, when n = 3, the function generates the numbers 2, 4, and 6, squares them to get 4, 16, and 36, and then sums them up to get 56. The function works for any positive integer n. 

Note: The range function in Python is exclusive of the end value, so 2 * n + 1 is used to include the last even number in the range. The step size 2 is used to generate only even numbers. 





Note: This problem is a variation of the "Squares of numbers" problem, where instead of summing the squares of all numbers up to n, we are summing the squares of the first n even numbers. The solution is similar, but with a slight modification to the range function to generate only even numbers.