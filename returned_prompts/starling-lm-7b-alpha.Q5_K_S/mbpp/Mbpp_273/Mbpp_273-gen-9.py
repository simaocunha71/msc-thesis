```
def substract_elements(tup1, tup2):
    return tuple(t[0] - t[1] for t in zip(tup1, tup2))
```

Explanation:

The function `substract_elements` takes in two tuples, `tup1` and `tup2`. It uses the `zip` function to pair up the corresponding elements of the two tuples. The `zip` function returns an iterable of tuples, where each tuple contains the element at the same index in `tup1` and `tup2`. 

The function then uses a generator expression to subtract the second element of each paired tuple from the first element of the paired tuple. The `t[0] - t[1]` expression calculates the difference between the two elements. 

Finally, the function returns a new tuple containing the subtracted elements. 

The provided assert statement tests the function by passing in the tuples `(10, 4, 5)` and `(2, 5, 18)`. The expected result is `(8, -1, -13)`. 

This solution effectively subtracts the elements of the first tuple by the elements of the second tuple with the same index, as required by the problem statement.

Note: The `zip` function is used to iterate over the tuples in `tup1` and `tup2` simultaneously, pairing up the corresponding elements at each index. The `t[0] - t[1]` expression calculates the difference between the first and second elements of each paired tuple. The `tuple()` function is used to create a new tuple containing the subtracted elements.
```
def substract_elements(tup1, tup2):
    return tuple(t[0] - t[1] for t in zip(tup1, tup2))
```
This function will return the expected result of `(8, -1, -13)` when given the tuples `(10, 4, 5)` and `(2, 5, 18)`.

Explanation:

The function `substract_elements` takes in two tuples, `tup