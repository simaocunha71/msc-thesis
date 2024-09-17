```
def index_multiplication(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(tuple(x * y for x, y in zip(t1[i], t2[i])))
    return tuple(result)
```


This function takes two tuples as input, performs index-wise multiplication of their elements, and returns the result as a tuple of tuples. It uses the built-in functions zip and tuple to iterate over the elements of the input tuples and the function map to perform the multiplication. The result is then returned as a tuple of tuples. The unit test provided in the problem description ensures that the function works correctly for the given input. For example, the test `assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))` checks that the function returns the correct result for the given input.