The problem is asking to create a function that takes two numbers as input and returns a tuple with the second number followed by the first number. 

Based on the unit test provided, `assert swap_numbers(10,20)==(20,10)`, it seems that the function should swap the order of the input numbers.

Here is a Python solution for the problem:
```
def swap_numbers(a, b):
    return (b, a)
```  # This function swaps the input numbers
```


This function works by directly returning a tuple with the second number `b` first and the first number `a` second. This is exactly what the problem asks for. The unit test `assert swap_numbers(10,20)==(20,10)` also confirms that this function works correctly.