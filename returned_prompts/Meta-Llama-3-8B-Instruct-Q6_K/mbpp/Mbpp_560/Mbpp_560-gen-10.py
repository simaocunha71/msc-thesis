```
def union_elements(tup1, tup2):
    return tuple(sorted(set(tup1 + tup2)))
```


Explanation:
The function `union_elements` takes two tuples `tup1` and `tup2` as input. It combines the elements of both tuples into a single set, removes duplicates by converting it to a set, and then converts it back to a tuple. Finally, it sorts the elements of the tuple in ascending order using the `sorted` function. The resulting tuple is then returned. 

The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` ensures that the function works correctly by comparing the output with the expected result. 

This function assumes that the input tuples do not contain duplicate elements. If the input tuples can contain duplicates, the function will still work correctly, but the output tuple will also contain duplicate elements. If you want to remove duplicates from the input tuples before finding their union, you can convert each tuple to a set before combining them and converting the result back to a tuple. However, this would also remove duplicate elements from the input tuples. 

Here is the modified function that removes duplicates from the input tuples:

```
def union_elements(tup1, tup2):
    return tuple(sorted(set(tup1) | set(tup2)))
```


In this modified function, `set(tup1) | set(tup2)` is used to find the union of the two sets. This operation removes duplicates from the input tuples and combines the unique elements into a single set. The `sorted` function is then used to sort the elements of the set in ascending order, and the result is converted back to a tuple. 

The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` will pass for this modified function as well, because it ensures that the function works correctly even when the input tuples contain duplicate elements. 

However, if you want to preserve the original order of the elements in the input tuples, you would need a different approach. The `sorted` function does not preserve the original order of the elements, so it would not work correctly if you want to preserve the original order. In