```
def min_of_three(a, b, c):
    return min(a, b, c)
```



The problem asks you to write a function that takes three numbers as input and returns the smallest of the three. 

The unit test `assert min_of_three(10,20,0)==0` suggests that the function should return the smallest number from the input. 

In Python, the built-in `min()` function can be used to find the smallest of multiple values. Therefore, the solution is simply to return the minimum of the three input numbers:

```
def min_of_three(a, b, c):
    return min(a, b, c)
```



This function will work correctly for any three input numbers and will return the smallest of the three. The unit test provided will also pass with this solution. 





Please note that this solution assumes that the input numbers are integers or can be compared using the less than (<) operator. If the input numbers are not comparable (for example, if they are strings), a more complex solution would be needed.