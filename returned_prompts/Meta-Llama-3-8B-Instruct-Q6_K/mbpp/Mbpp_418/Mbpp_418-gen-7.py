```
def Find_Max(lst):
    return max(lst, key=len)
```


This function uses the built-in max function in Python, which returns the item with the maximum value. The key argument of the max function is used to specify a function of one argument that is used to extract a comparison key from each input element. In this case, the key is the length of each sublist. The max function returns the sublist with the maximum length. 

The unit test `assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']` ensures that the function works correctly. It checks that the function returns the sublist with the maximum length, which is `['A','B','C']`. 





