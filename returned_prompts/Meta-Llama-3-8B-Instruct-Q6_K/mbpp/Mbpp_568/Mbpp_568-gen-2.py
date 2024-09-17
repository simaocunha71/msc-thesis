```
def empty_list(N):
    return [{},]*N
```


The unit test `assert empty_list(5)==[{},{},{},{},{}]` suggests that the function should create a list of N empty dictionaries. The function `empty_list(N)` can be implemented using list multiplication. This is a common idiom in Python where `[]` is repeated N times to create a list of N empty lists. In this case, `[]` is replaced with `{}` to create a list of N empty dictionaries. The result is a list of N empty dictionaries. 

The function can be written as follows:

```
def empty_list(N):
    return [{},]*N
```

This function works by creating an empty dictionary and then multiplying it N times to create a list of N empty dictionaries. This is a simple and efficient way to create a list of N empty dictionaries. 





