```
def sum_list(a,b):
    return [x+y for x,y in zip(a,b)]
```


This function uses list comprehension to iterate over the input lists `a` and `b` simultaneously using the `zip` function. For each pair of elements `(x,y)`, it adds them together and returns a new list with the results. 

The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` ensures that the function works correctly. 

This function assumes that both input lists have the same length. If the lists have different lengths, the function will stop when it reaches the end of the shorter list. If you want to handle lists of different lengths, you could add some error checking code. 





C:
```
def sum_list(a,b):
    if len(a) != len(b):
        raise ValueError("Lists must have the same length")
    return [x+y for x,y in zip(a,b)]
```


In this version, I added a check at the beginning of the function to ensure that the input lists have the same length. If they don't, the function raises a `ValueError`. This way, the function will fail quickly if the input lists are of different lengths, rather than producing incorrect results.