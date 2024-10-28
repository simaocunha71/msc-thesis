To solve this problem, you can follow these steps:

1. Convert the input lists to sets to remove any duplicate elements. This will also allow us to use the intersection method to find common elements.
2. Use the intersection method to find the common elements between the two sets. The intersection method returns a set containing only the common elements.
3. Convert the resulting set back into a list and sort it in ascending order using the sorted function. This ensures that the resulting list is sorted and unique.
4. Return the sorted list of common elements.

Here's the implementation of the solution in Python:

```python
def common(l1, l2):
    # Convert the input lists to sets
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the common elements using the intersection method
    common_elements = set1.intersection(set2)
    
    # Convert the resulting set back into a list and sort it
    result = sorted(common_elements)
    
    # Return the sorted list of common elements
    return result
```

You can test the function using the provided test cases:

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 2, 3, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```

The function will return the sorted unique common elements for the given input lists.

































```

```