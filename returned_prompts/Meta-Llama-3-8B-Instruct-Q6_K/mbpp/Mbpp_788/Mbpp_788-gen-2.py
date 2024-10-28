```
def new_tuple(lst, str):
    return tuple(lst + [str])
```


This function takes a list and a string as arguments, and returns a new tuple that is the concatenation of the list and the string. The unit test `assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')` ensures that the function works correctly. 

The `+` operator can be used to concatenate a list and a list-like object (such as a string). The `tuple` function is then used to convert the resulting list to a tuple. 

For example, if you call `new_tuple(["WEB", "is"], "best")`, it will return the tuple `('WEB', 'is', 'best')`. 
```
print(new_tuple(["WEB", "is"], "best"))
```


Output:
```
('WEB', 'is', 'best')
``` 







