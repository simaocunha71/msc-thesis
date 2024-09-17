```
def extract_even(t):
    new_t = []
    for i in t:
        if isinstance(i, tuple):
            new_t.append(extract_even(i))
        elif i % 2 == 0:
            new_t.append(i)
    return tuple(new_t)
```
The function `extract_even` takes a nested mixed tuple as input and returns a new tuple with all the uneven elements removed. It uses a recursive approach to traverse the tuple and its nested tuples. For each element, it checks if the element is a tuple. If it is, it calls the function `extract_even` on that tuple. If the element is not a tuple and it's an even number, it adds it to the new tuple. The function finally returns the new tuple. 

For example, if we call `extract_even((4, 5, (7, 6, (2, 4)), 6, 8))`, it will return `(4, (6, (2, 4)), 6, 8)`, which is the input tuple with all the uneven elements removed. 

The unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` ensures that the function works correctly. 

This function assumes that the input is a valid nested mixed tuple. If the input is not a tuple or contains non-integer values, the function may not work correctly.  In a real-world scenario, you would want to add error checking to handle these cases.  Also, this function does not handle infinite recursion, which could occur if the input tuple contains a cycle of nested tuples.  In a real-world scenario, you would want to add a maximum recursion depth to prevent this.  Finally, this function does not handle the case where the input tuple contains non-integer values that are not even or uneven.  In a real-world scenario, you would want to add a check for this and decide how to handle it.  For example, you could raise an error or ignore the non-integer values.  The best approach depends on the specific requirements of your application.  The function as written will simply ignore the non-integer values.  This may or may not be the desired behavior, depending on your application.  If you want to raise an error instead, you could modify the function to raise an error if it