```
def Find_Max(lst):
    max_len = max(len(i) for i in lst)
    return max([i for i in lst if len(i) == max_len])
```


Explanation: 
The function `Find_Max` takes a list of lists as input. It finds the maximum length of the sublists using a generator expression inside the `max` function. Then it uses a list comprehension to find the sublist with the maximum length and returns it. 

The unit test `assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']` ensures that the function is working correctly. It checks if the function returns the sublist with the maximum length, which in this case is `['A','B','C']`. 





