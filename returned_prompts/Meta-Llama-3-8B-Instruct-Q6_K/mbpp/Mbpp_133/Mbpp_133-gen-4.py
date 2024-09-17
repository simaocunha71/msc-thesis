```
def sum_negativenum(lst):
    return sum([x for x in lst if x < 0])
```


The unit test provided ensures that the function should return the sum of the negative numbers in the list. The given unit test is `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32`. 

This problem can be solved by using a list comprehension to generate a list of negative numbers and then summing up this list. The list comprehension `[x for x in lst if x < 0]` generates a list of all negative numbers in the list. The `sum` function then adds up these negative numbers. 

This solution passes the given unit test. 

Note: The problem description doesn't specify what to do with the remaining elements in the list, but based on the unit test, it seems that the function should return the sum of all negative numbers in the list. If the problem description was intended to mean something else, the solution would need to be adjusted accordingly. 