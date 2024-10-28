```
def opposite_Signs(a, b):
    return (a > 0) != (b > 0)
```


The function `opposite_Signs` takes two integers `a` and `b` as input and returns `True` if they have opposite signs, and `False` otherwise.

The condition `(a > 0) != (b > 0)` checks whether the signs of `a` and `b` are opposite. If `a` is positive and `b` is negative, or vice versa, this condition will be `True`. Otherwise, it will be `False`. 

This function is tested with the unit test `assert opposite_Signs(1,-2) == True`, which checks whether the function returns `True` when the inputs are `1` and `-2`. 

This function can be used in a variety of contexts, such as checking whether the sum of two numbers is zero, or whether the average of two numbers is zero, or whether the product of two numbers is negative, and so on. 

For example, you can use this function to check whether the sum of two numbers is zero by using the condition `opposite_Signs(a, b) and a + b == 0`. This will return `True` if the sum of `a` and `b` is zero and they have opposite signs, and `False` otherwise. 

Similarly, you can use this function to check whether the average of two numbers is zero by using the condition `opposite_Signs(a, b) and (a + b) / 2 == 0`. This will return `True` if the average of `a` and `b` is zero and they have opposite signs, and `False` otherwise. 

And so on. The possibilities are endless!