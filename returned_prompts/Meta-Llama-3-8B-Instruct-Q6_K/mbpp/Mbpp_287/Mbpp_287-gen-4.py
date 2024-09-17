```
def square_Sum(n):
    return sum([i ** 2 for i in range(2, 2 * n + 1, 2)])
```





This function generates a list of squares of even numbers from 2 to 2n (inclusive) and then returns the sum of these squares. The unit test `assert square_Sum(2) == 20` helps in understanding the problem better, as it implies that the function should return the sum of squares of all even numbers up to 2n. The unit test also ensures that the function is working correctly for n=2.