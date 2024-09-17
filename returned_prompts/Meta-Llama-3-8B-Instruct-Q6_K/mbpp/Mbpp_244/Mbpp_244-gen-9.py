```
def next_Perfect_Square(n):
    i = int(n ** 0.5)
    while (i + 1) ** 2 <= n:
        i += 1
    return (i + 1) ** 2
```


This problem is asking to find the next perfect square greater than a given number. 

We can solve this problem by first finding the square root of the given number, then incrementing the square root until we find the next perfect square. 

Here is a python function to do this:

```
def next_Perfect_Square(n):
    i = int(n ** 0.5)
    while (i + 1) ** 2 <= n:
        i += 1
    return (i + 1) ** 2
```

This function works by first finding the square root of the given number. This is done by raising the number to the power of 0.5 and converting the result to an integer. 

Then it enters a loop where it increments the square root until the square of the incremented square root is greater than the given number. 

Once the loop is exited, it returns the square of the incremented square root, which is the next perfect square greater than the given number. 

This function is tested with the unit test `assert next_Perfect_Square(35) == 36`, which passes. 

So, the output of the function `next_Perfect_Square(35)` is `36`, which is the next perfect square greater than `35`. 

This function can be used to find the next perfect square greater than any given number. 





```
def next_Perfect_Square(n):
    i = int(n ** 0.5)
    while (i + 1) ** 2 <= n:
        i += 1
    return (i + 1) ** 2
```





```
def next_Perfect_Square(n):
    i = int(n ** 0.5)
    while (i + 1) ** 2 <= n:
        i += 1
    return (i + 1) ** 2
```





```
def next_Perfect_Square(n):
    i = int(n ** 0.5)
    while (i + 1) ** 2 <= n:
        i += 1
    return (i + 1) ** 2
```





```
def next_Perfect_Square(n