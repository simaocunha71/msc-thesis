```
def all_unique(lst):
    s = set()
    for i in lst:
        if i in s:
            return False
        s.add(i)
    return True
```

Explanation:

In this Python function, we use a set `s` to keep track of the unique elements we have encountered so far. We iterate through the input list `lst` and for each element `i`, we check if it is already in the set `s`. If it is, then we have encountered a duplicate element and the function returns False. Otherwise, we add the element to the set. Once we have iterated through the entire input list, we can conclude that all elements are unique and the function returns True.

The `assert all_unique([1,2,3]) == True` is a way to check if the function is working correctly. It asserts that when the function is called with the input `[1,2,3]`, it should return True, as all the elements in this list are indeed unique. If the function does not return True, the assertion will fail and an error message will be raised.

Overall, this function provides a simple and efficient way to check if the elements of a given list are unique or not.

Note: It's worth mentioning that if you're using Python 3.7 or later, you can also use the built-in `len(set(lst)) == len(lst)` expression to check if all elements in the list are unique. However, the function provided here is more explicit and can be more useful in cases where you need to perform additional operations on the set during the process, such as checking if the set contains specific elements or performing custom operations on the elements.

Here's an example of how you can use the `all_unique` function:

```python
def all_unique(lst):
    s = set()
    for i in lst:
        if i in s:
            return False
        s.add(i)
    return True

# Testing the function
print(all_unique([1,2,3]))  # Output: True
print(all_unique([1,2,2]))  # Output: False
```

In the first test case, the function correctly identifies