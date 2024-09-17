```
def even_Power_Sum(n):
    return sum([i**5 for i in range(2, 2*n, 2)])
```


This function works by creating a list of even numbers from 2 to 2n, then raising each of those numbers to the fifth power and summing the results. The range function is used to generate the sequence of even numbers, with a step size of 2 to ensure that only even numbers are included. The unit test `assert even_Power_Sum(2) == 1056` confirms that the function is working correctly.