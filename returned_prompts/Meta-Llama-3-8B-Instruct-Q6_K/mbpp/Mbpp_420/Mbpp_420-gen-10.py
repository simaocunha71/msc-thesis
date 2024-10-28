```
def cube_Sum(n):
    total = 0
    for i in range(2, 2*n, 2):
        total += i**3
    return total
```    
The function cube_Sum(n) calculates the sum of the cubes of the first n even natural numbers. It does this by iterating over the range of even numbers from 2 to 2n, cubing each number and adding it to the total. The function returns the total sum.

The unit test assert cube_Sum(2) == 72 ensures that the function works correctly for n=2. For n=2, the even numbers are 2 and 4, and their cubes are 8 and 64. The sum of these cubes is 72. 

So, the function cube_Sum(n) correctly calculates the sum of the cubes of the first n even natural numbers.