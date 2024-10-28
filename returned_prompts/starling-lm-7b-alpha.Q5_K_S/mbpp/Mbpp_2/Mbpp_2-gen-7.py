```python
def similar_elements(list1,list2):
    return list(set(list1) & set(list2))

assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
```

Explanation:
In this program, we define a function called similar_elements that takes two lists as parameters. The function uses the set() function to convert the lists into sets, and then uses the & operator to find the intersection of the two sets. Finally, the function converts the intersection back into a list using the list() function and returns it.

The assert statement is used to verify that the function is working correctly. It checks if the set returned by the function is equal to the set (4, 5), which is the expected result for the given input lists.

Overall, this program defines a function that finds the shared elements between two lists and returns them as a list.

In the given example, the function is called with the input lists (3, 4, 5, 6) and (5, 7, 4, 10). The expected result is the set (4, 5), which represents the shared elements between the two lists. The assert statement checks if the actual result matches the expected result.
```

```python
def similar_elements(list1,list2):
    return list(set(list1) & set(list2))

print(similar_elements([3, 4, 5, 6],[5, 7, 4, 10]))
```

Explanation:
In this program, we define a function called similar_elements that takes two lists as parameters. The function uses the set() function to convert the lists into sets, and then uses the & operator to find the intersection of the two sets. Finally, the function converts the intersection back into a list using the list()