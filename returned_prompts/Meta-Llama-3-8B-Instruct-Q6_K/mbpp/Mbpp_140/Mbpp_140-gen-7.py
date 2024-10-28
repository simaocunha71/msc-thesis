```
def extract_singly(lst):
    result = set()
    for item in lst:
        if isinstance(item, list):
            result.update(extract_singly(item))
        else:
            result.add(item)
    return result
```



This problem requires you to write a function that takes a list of lists as input and returns a set of unique numbers. The list of lists can contain both integers and other lists. The function should recursively traverse the list of lists, adding each integer to the set.

The unit test `assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])` helps to clarify the problem by providing an example of the expected output.

Here's the solution in Python:
```
def extract_singly(lst):
    result = set()
    for item in lst:
        if isinstance(item, list):
            result.update(extract_singly(item))
        else:
            result.add(item)
    return result
```
This function uses a set to keep track of the unique numbers. It iterates over the input list, and for each item, it checks if the item is a list. If it is, the function calls itself recursively with the sublist as the new input. If the item is not a list, the function adds it to the set. Finally, the function returns the set of unique numbers.