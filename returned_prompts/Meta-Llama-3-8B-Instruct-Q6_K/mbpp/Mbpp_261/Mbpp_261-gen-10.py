```
def division_elements(tuple1, tuple2):
    result = []
    for i in range(len(tuple1)):
        if tuple2[i] != 0:
            result.append(tuple1[i] / tuple2[i])
        else:
            result.append(None)
    return tuple(result)
```


The function takes two tuples as input and performs element-wise division. It iterates over the length of the first tuple and divides each element by the corresponding element in the second tuple. If the second tuple element is zero, the result is set to None. The function returns a new tuple with the division results. 

The unit test `assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)` ensures that the function works as expected. 

Note: This function assumes that the input tuples are of the same length. If the tuples are of different lengths, the function will throw an error. You may want to add error handling or input validation to handle such cases. 







