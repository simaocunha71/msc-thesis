The nth octagonal number is given by the formula (9n^2 - 1)/2. So, we can write a function to find the nth octagonal number as follows:

```python
def is_octagonal(n):
    return (9*n**2 - 1)//2
```

This function takes an integer n as input and returns the nth octagonal number. The formula (9n^2 - 1)/2 is used to calculate the nth octagonal number. The "//" operator is used for integer division in Python. 

For example, the 5th octagonal number is 65, which is calculated by the function is_octagonal(5) as follows:

```python
is_octagonal(5) == (9*5**2 - 1)//2 == 65
```  