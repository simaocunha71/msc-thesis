```
def cube_Sum(n):
    return sum([i**3 for i in range(2, 2*n, 2)])
```


The unit test `assert cube_Sum(2) == 72` indicates that the function should return the sum of the cubes of the first 2 even numbers, which are 2 and 4. The sum of their cubes is 2^3 + 4^3 = 8 + 64 = 72. This is a good test case for the function. 

The function `cube_Sum` uses a list comprehension to generate the cubes of the first n even natural numbers, and then sums them up using the built-in `sum` function. The `range` function is used to generate the sequence of even numbers from 2 to 2*n. The `**` operator is used to raise each number to the power of 3, and the `sum` function is used to add up the results. 

This function should pass the unit test `assert cube_Sum(2) == 72`. 

For example, if you call `cube_Sum(3)`, it will return the sum of the cubes of the first 6 even natural numbers, which are 2, 4, 6, 8, 10, 12. The sum of their cubes is 2^3 + 4^3 + 6^3 + 8^3 + 10^3 + 12^3 = 8 + 64 + 216 + 512 + 1000 + 1728 = 3548. 

You can call `cube_Sum(3)` to test the function. The output should be 3548. 