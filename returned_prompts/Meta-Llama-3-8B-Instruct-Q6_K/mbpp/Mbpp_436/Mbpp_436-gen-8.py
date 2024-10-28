```
def neg_nos(lst):
    return [i for i in lst if i < 0]
```


The function neg_nos takes a list as an argument and returns a new list containing all the negative numbers from the original list. This is achieved by using a list comprehension that iterates over the list and includes a number in the new list if it is less than 0.

The unit test `assert neg_nos([-1,4,5,-6]) == [-1,-6]` ensures that the function works correctly, as it checks that the output of neg_nos([-1,4,5,-6]) is indeed [-1,-6]. 

This function can be used with any list, not just the one provided in the unit test. For example, `neg_nos([1,2,3,-4,-5,-6])` would return `[-4,-5,-6]`. 

The function does not modify the original list, it returns a new list containing the negative numbers. This is a good practice as it avoids modifying the original data unintentionally. 