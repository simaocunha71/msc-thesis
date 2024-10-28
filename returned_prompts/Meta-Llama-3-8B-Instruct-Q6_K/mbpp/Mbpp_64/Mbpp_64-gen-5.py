```
def subject_marks(tuples):
    return sorted(tuples, key=lambda x: x[1])
```

This function uses the built-in `sorted` function in Python, which sorts the input list of tuples based on the key provided. The key is a function that takes a tuple and returns its second value (index 1). The `sorted` function then sorts the list of tuples based on these values. The default sorting order is ascending, so the tuples with the lower second values will come first. 

The unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` demonstrates that the function correctly sorts the list of tuples based on the second value of each tuple. 

The function does not modify the original list, it returns a new sorted list. If you want to modify the original list, you can use the `sort` method instead of `sorted` function. The `sort` method sorts the list in-place. 

Note: The problem statement does not specify the sorting order. However, based on the unit test provided, it seems that the default sorting order (ascending) is intended. If you want to sort the list in descending order, you can use the `sorted` function with the `reverse=True` argument. For example: `return sorted(tuples, key=lambda x: x[1], reverse=True)`. 