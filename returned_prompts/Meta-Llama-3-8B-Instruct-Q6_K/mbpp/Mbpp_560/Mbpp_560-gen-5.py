```
def union_elements(tup1, tup2):
    return tuple(set(tup1 + tup2))
```
The function `union_elements` takes two tuples as input and returns a new tuple that contains all unique elements from both input tuples. The set data structure is used to remove duplicates and then the result is converted back to a tuple. The order of the elements in the output tuple is not guaranteed to be the same as the order in the input tuples. 

For example, `union_elements((3, 4, 5, 6),(5, 7, 4, 10))` returns `(3, 4, 5, 6, 7, 10)`. 

However, the problem statement asks for the output to be in sorted order. To achieve this, we can sort the output tuple. Here's how you can modify the function:
```
def union_elements(tup1, tup2):
    return tuple(sorted(set(tup1 + tup2)))
``` 
This function will return the union of the elements of two given tuples in sorted order. For example, `union_elements((3, 4, 5, 6),(5, 7, 4, 10))` returns `(3, 4, 5, 6, 7, 10)`. 
The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` also confirms that the output is in sorted order. 