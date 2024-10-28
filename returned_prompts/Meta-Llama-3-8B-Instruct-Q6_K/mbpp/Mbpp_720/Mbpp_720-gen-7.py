```
def add_dict_to_tuple(tup, dict_obj):
    return tup + (dict_obj,)
```
The unit test `assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})` suggests that we should add the dictionary as a single element to the tuple. This can be done by using the tuple concatenation operator `+` and the tuple constructor `()` with the dictionary as the argument. The `+` operator concatenates tuples, and the `()` constructor converts the dictionary to a tuple. 

This solution is straightforward and follows the unit test's expected output. It does not modify the original tuple, but returns a new tuple with the dictionary added to it. This is in line with the problem's requirements. 

Note that this solution assumes that the dictionary is a single object that should be added to the tuple. If you want to add the dictionary's items as separate elements in the tuple, you would need to modify the solution accordingly. For example, you could use a list comprehension to convert the dictionary's items to a tuple and then concatenate it with the original tuple. However, this would not match the unit test's expected output. 