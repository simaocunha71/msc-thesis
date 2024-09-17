```
def index_multiplication(t1, t2):
    result = []
    for a, b in zip(t1, t2):
        result.append(tuple(x*y for x, y in zip(a, b)))
    return tuple(result)
```


Test:
```
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
```


Explanation:
The problem is asking to create a function that takes two tuples as input and returns a new tuple where each element is the product of the corresponding elements in the input tuples. The function should work for tuples of tuples and zip the input tuples based on their length.

The unit test provided ensures that the function works correctly by testing it with a specific input and expected output.

The solution uses the built-in zip function to iterate over the elements of the input tuples in parallel. It then uses a list comprehension to calculate the product of each pair of elements and converts the result to a tuple. The result is then returned as the output of the function.