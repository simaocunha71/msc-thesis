To find the difference between two lists, we can use list comprehension. Here's a step-by-step guide to help you understand how to achieve this:

1. First, define a function called "Diff" that takes two lists as arguments: list1 and list2.
2. Inside the function, use the "set" data structure to remove any duplicate elements in the lists. Since sets can only contain unique elements, this step will ensure that the same element doesn't appear twice in the final result.
3. Next, calculate the symmetric difference between list1 and list2 using the "symmetric_difference" method available for sets in Python. This method returns a new set that contains elements from either list1 or list2, but not both.
4. Finally, convert the set to a list using the "list" function and return the result.
5. To test the function, you can use the "assert" statement to verify if the output of the function matches the expected result. In this case, the expected result is [10, 20, 30, 15].

Here's the code that implements the solution:

```python
def Diff(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))
```

By running this code, you should get the expected result of [10, 20, 30, 15] when calling the "Diff" function with the provided lists.

```python
assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
```

This assertion will pass if the function returns the correct result, indicating that the implementation is correct.

"""

def Diff(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))

assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 