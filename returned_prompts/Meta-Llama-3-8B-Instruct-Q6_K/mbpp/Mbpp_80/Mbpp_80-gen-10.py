The nth tetrahedral number is the sum of the first n natural numbers. This can be calculated using the formula n*(n+1)*(n+2)/6. Here is the Python function to calculate the nth tetrahedral number:

```
def tetrahedral_number(n):
    return n*(n+1)*(n+2)//6
```

This function works by taking the input n and calculating the nth tetrahedral number using the formula. The result is returned as the output of the function. The unit test `assert tetrahedral_number(5) == 35` ensures that the function is working correctly. 

For example, the first five tetrahedral numbers are 1, 4, 10, 20, and 35, which can be calculated by the function `tetrahedral_number(1)`, `tetrahedral_number(2)`, `tetrahedral_number(3)`, `tetrahedral_number(4)`, and `tetrahedral_number(5)`, respectively. The function can be used to calculate any tetrahedral number. 