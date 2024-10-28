```
def get_equal(tuples):
    return len(set(len(t) for t in tuples)) == 1
```
The function `get_equal` takes a list of tuples as input and returns `True` if all tuples have the same length, and `False` otherwise. The function uses a generator expression to create a set of lengths from the input tuples. If the set has only one element, then all tuples have the same length, so the function returns `True`. Otherwise, it returns `False`. For example, the function `get_equal([(11, 22, 33), (44, 55, 66)])` returns `True` because both tuples have the same length, 3. The unit test `assert get_equal([(11, 22, 33), (44, 55, 66)]) == True` verifies this behavior.