The nth tetrahedral number is the sum of the first n natural numbers. It can be calculated using the formula n*(n+1)*(n+2)/6.

Here is the Python function to calculate the nth tetrahedral number:

```
def tetrahedral_number(n):
    return n*(n+1)*(n+2)//6
```

This function takes an integer n as input and returns the nth tetrahedral number. The function uses the formula n*(n+1)*(n+2)/6 to calculate the tetrahedral number. The // operator is used to perform integer division, which ensures that the result is an integer.

The unit test `assert tetrahedral_number(5) == 35` ensures that the function is working correctly. The function returns the correct tetrahedral number for n=5, which is 35.