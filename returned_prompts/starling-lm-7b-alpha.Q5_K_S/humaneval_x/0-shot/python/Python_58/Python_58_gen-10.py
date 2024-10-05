To solve this problem, we need to follow these steps:

1. Convert the lists to sets to remove duplicate elements.
2. Convert the sets to lists to make them iterable.
3. Use the `set.intersection()` method to find the common elements.
4. Sort the common elements in ascending order using the `sorted()` function.
5. Return the sorted common elements.

Here's the step-by-step solution:

```python
def common(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
    common_set = l1_set & l2_set
    common_list = sorted(common_set)
    return common_list
```

Now, let's test the function with the provided test cases:

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```

The function correctly returns the sorted unique common elements for the given input lists.

Note: This solution assumes that the input lists contain only hashable elements (i.e., no dictionaries, classes, etc.).

In Python, a dictionary is a collection of key-value pairs, where each key is unique. A set is a collection of unique elements, which means it cannot contain duplicate values. By converting the lists to sets, we can eliminate duplicate elements and then find the common elements using the `set.intersection()` method. Finally, we sort the common elements in ascending order using the `sorted()` function and return the result.

The time complexity of this solution is O(n log n), where n is the total number of elements in both lists. This is because converting the lists to sets and finding the intersection both have a time complexity of O(n log n). Sorting the common elements takes O(n log n) time as well. Therefore, the overall