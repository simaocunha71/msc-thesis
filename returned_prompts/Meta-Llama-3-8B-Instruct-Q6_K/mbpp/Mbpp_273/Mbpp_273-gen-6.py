The problem is asking to write a function that subtracts the elements of the first tuple by the elements of the second tuple with the same index. 

For example, if the input tuples are (10, 4, 5) and (2, 5, 18), the output should be (8, -1, -13).

Here is a Python function that solves this problem:

```
python
def substract_elements(t1, t2):
    return tuple(x - y for x, y in zip(t1, t2))
```

This function uses the built-in `zip` function to iterate over the two tuples in parallel, and the `tuple` function to convert the result back into a tuple. The `x - y` expression subtracts the elements of the second tuple from the elements of the first tuple.

This function passes the given unit test:

```
python
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
```  