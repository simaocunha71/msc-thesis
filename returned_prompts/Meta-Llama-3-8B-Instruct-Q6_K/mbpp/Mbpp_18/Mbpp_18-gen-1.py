You can use the set difference operation to remove characters from the first string which are present in the second string. The set difference operation in Python is denoted by the `-` operator. It returns a new set with elements in the set that are not present in another set.

Here is the Python function that implements this:

```Python
def remove_dirty_chars(s, dirty_chars):
    return ''.join([c for c in s if c not in dirty_chars])
```

This function uses a list comprehension to create a new list of characters that are not in the `dirty_chars` string, and then joins this list into a new string using the `join` method. The `assert` statement in the problem ensures that this function works correctly. For example, `remove_dirty_chars("probasscurve", "pros")` should return `'bacuve'`. 

The time complexity of this function is O(n), where n is the length of the input string, because it needs to iterate over the entire string. The space complexity is also O(n), because it needs to create a new string that is the same length as the input string. 





