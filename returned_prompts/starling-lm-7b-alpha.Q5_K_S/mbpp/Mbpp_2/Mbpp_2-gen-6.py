```
def similar_elements(a,b):
    return set(a) & set(b)
```

The above code defines a function `similar_elements` that takes two lists as input. It uses the `set()` function to convert the input lists to sets, and then uses the `&` operator to find the intersection of the two sets, which gives us the shared elements. Finally, it converts the resulting set to a set again using the `set()` function, and returns it.

To test the function, you can use the `assert` statement to check if the output of `set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))` is equal to the expected result `set((4, 5))`. If the assertion is true, it means that the function is correctly finding the shared elements from the given two lists.

The `set()` function is used here to convert the input lists to sets, which automatically removes duplicate elements from the lists, and allows us to easily find the intersection of the two sets using the `&` operator.

Overall, this solution provides a concise and efficient way to find the shared elements from two lists in Python.

```python
def similar_elements(a,b):
    return set(a) & set(b)
```

To use this solution, you can define a function `similar_elements` that takes two lists `a` and `b` as input. The function uses the `set()` function to convert the input lists to sets, and then uses the `&` operator to find the intersection of the two sets, which gives us the shared elements. Finally, it converts the resulting set to a set again using the `set()` function, and returns it.

To test the function, you can use the `assert` statement to check if the output of `set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))` is equal to the expected result `set((4, 5))`. If the assertion is true, it means that the function is correctly finding the shared elements from the given two lists.

The `set()` function is used here to convert the