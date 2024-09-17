You can solve this problem by creating a new dictionary and iterating over the items in the given dictionary. If the value of a key-value pair is not None, you add it to the new dictionary.

Here is the Python function that solves the problem:
```
def drop_empty(d):
    return {key: value for key, value in d.items() if value is not None}
```
This function uses a dictionary comprehension to create a new dictionary that only includes the key-value pairs where the value is not None. The `items()` method is used to iterate over the key-value pairs in the dictionary, and the `if value is not None` condition is used to filter out the pairs where the value is None. The resulting dictionary is then returned.

The unit test `assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}` ensures that the function correctly drops the key-value pair with a None value from the dictionary. It checks that the function returns a dictionary with only the 'c1' and 'c2' key-value pairs, and that the 'c3' key-value pair is not present in the returned dictionary. If the function correctly implements the desired behavior, the unit test will pass.