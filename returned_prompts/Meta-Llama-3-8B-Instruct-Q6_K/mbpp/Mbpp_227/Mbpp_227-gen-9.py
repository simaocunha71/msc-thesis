```
def min_of_three(a, b, c):
    return min(a, b, c)
```
The problem is asking you to write a function that takes three numbers as input and returns the smallest one. 

The unit test `assert min_of_three(10,20,0)==0` suggests that the function should return the smallest number among the three input numbers. 

In Python, you can use the built-in `min` function to find the smallest number among three or more numbers. So, the solution is quite simple: just return the result of `min(a, b, c)`. 

Note: The function `min` returns the smallest item in an iterable or the smallest of two or more arguments. It is a built-in function in Python.  It can be used with multiple arguments, not just with a list. For example, `min(a, b, c)` will return the smallest of `a`, `b`, and `c`.  If there are multiple smallest items, the function returns one of them.  If you want to get all the smallest items, you can convert the arguments to a list and then use the function with the list.  For example, `min([a, b, c])` will return the smallest of `a`, `b`, and `c`.  If `a`, `b`, and `c` are all the same, then both `min(a, b, c)` and `min([a, b, c])` will return `a`.  If `a`, `b`, and `c` are not all the same, then `min(a, b, c)` will return one of the smallest items, and `min([a, b, c])` will return one of the smallest items.  If you want to get all the smallest items, you can convert the arguments to a list and then use the function with the list.  For example, `min([a, b, c])` will return the smallest of `a`, `b`, and `c`.  If `a`, `b`, and `c` are all the same, then both `min(a, b, c)` and `min([a, b, c])` will return `a`.  If `a`, `b`, and `c` are not all the same, then `min(a, b, c)` will return one of the smallest items, and `min([a, b, c])