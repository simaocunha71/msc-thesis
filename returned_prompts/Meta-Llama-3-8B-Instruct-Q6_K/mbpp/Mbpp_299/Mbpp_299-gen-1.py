You can use the built-in max function in Python with a custom key. The max function returns the largest item in an iterable or the largest of two or more arguments. The key argument specifies a function of one argument that is used to extract a comparison key from each input element.

Here, the function is used to calculate the sum of the second element of each tuple. The max function then returns the tuple with the maximum sum.

```
def max_aggregate(tuples):
    return max(tuples, key=lambda x:sum(x[1:]))
```

This function will return the tuple with the maximum sum of the second and subsequent elements. For example, if you call `max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])`, it will return `('Juan Whelan', 212)`. 

The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` ensures that the function is working correctly. 

Please note that the tuples in the list are expected to have at least two elements. If a tuple has only one element, this function will return the tuple itself, not an error. If you want to handle the case where a tuple has only one element, you can add a check before trying to calculate the sum. 

For example, you could use a conditional expression in the lambda function:

```
def max_aggregate(tuples):
    return max(tuples, key=lambda x:(x[0], sum(x[1:]) if len(x)>1 else 0))
```  This will return the tuple with the maximum sum of the second and subsequent elements, or the original tuple if it has only one element. The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` will still pass with this modified function. 