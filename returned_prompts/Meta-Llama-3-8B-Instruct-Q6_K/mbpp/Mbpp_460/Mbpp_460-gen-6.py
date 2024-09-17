def Extract(sublists):
    return [x[0] for x in sublists]  # Use list comprehension to extract the first element of each sublist.

# Test the function
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))  # Output: [1, 3, 6]
```

This Python function `Extract` takes a list of sublists as an input and returns a new list containing the first element of each sublist. It uses a list comprehension to achieve this. The list comprehension iterates over each sublist in the input list, and for each sublist, it extracts the first element using `x[0]`. The resulting elements are collected into a new list, which is then returned.

The unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` ensures that the function works correctly for the given input. When you run this function with the provided input, it should return the expected output `[1, 3, 6]`. 

The function is generic and can be used with any list of sublists, not just the one provided in the unit test. It's a simple and efficient way to extract the first element from each sublist in a list of sublists. 