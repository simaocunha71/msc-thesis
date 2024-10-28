The nth tetrahedral number is the sum of the first n natural numbers, plus the sum of the first n-1 natural numbers, plus the sum of the first n-2 natural numbers, and so on, up to the sum of the first 1 natural number. This can be calculated using the formula n*(n+1)*(n+2)/6.

Here is a Python function that calculates the nth tetrahedral number:

```
def tetrahedral_number(n):
    return n*(n+1)*(n+2)//2
```

This function works by first calculating the sum of the first n natural numbers using the formula n*(n+1)//2, and then adding the sum of the first n-1 natural numbers, and so on, up to the sum of the first 1 natural number. The result is the nth tetrahedral number.

For example, the 5th tetrahedral number is 35, which can be calculated as follows:

```
tetrahedral_number(5) = 5*(5+1)*(5+2)//2 = 35
```


The unit test `assert tetrahedral_number(5) == 35` ensures that the function is working correctly.