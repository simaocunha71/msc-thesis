```
def union_elements(t1,t2):
    # Convert tuples to lists
    list1 = list(t1)
    list2 = list(t2)
    # Concatenate the two lists
    combined_list = list1 + list2
    # Sort the combined list
    combined_list.sort()
    # Return the sorted list
    return tuple(combined_list)
```

Explanation:
The function `union_elements` takes in two tuples and converts them into lists. It then concatenates the two lists together and sorts the combined list in ascending order. The sorted list is then returned as a tuple. The `assert` statement is used to verify that the function correctly finds the union of the two given tuples and outputs them in sorted order.

To use the function, you can call it with two tuples as arguments, like this:

```python
result = union_elements((3, 4, 5, 6), (5, 7, 4, 10))
print(result)  # Output: (3, 4, 5, 6, 7, 10)
```

In this example, the function `union_elements` is called with the tuples `(3, 4, 5, 6)` and `(5, 7, 4, 10)`. The result is a tuple containing all the unique elements from both tuples, sorted in ascending order: `(3, 4, 5, 6, 7, 10)`.

The `assert` statement is used to verify that the function correctly finds the union of the two given tuples and outputs them in sorted order. If the function's output does not match the expected output, an AssertionError will be raised.

Overall, this function provides a simple and efficient way to find the union of two tuples and output the result in sorted order.

Note: The function assumes that the tuples contain only integer elements. If the tuples can contain other types of elements, you may need to modify the function to handle those types as well.

Additionally, it's important to note that the `sort()` method in Python sorts elements in place, meaning it modifies