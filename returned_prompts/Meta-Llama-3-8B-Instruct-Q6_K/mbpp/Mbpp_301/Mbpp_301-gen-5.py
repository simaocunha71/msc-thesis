The problem is asking for a function that calculates the depth of a dictionary. The depth of a dictionary is the maximum number of nested dictionaries it contains.

Here's a Python solution for this problem:

```
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    depth = 1
    for k, v in d.items():
        depth = max(depth, 1 + dict_depth(v))
    return depth
```

This function works by recursively going through each key-value pair in the dictionary. If the value is another dictionary, it calls itself with that dictionary and adds 1 to the depth. The maximum depth found during the recursion is the depth of the original dictionary. If the value is not a dictionary, it simply returns 0 for that key-value pair.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` shows that the function should return 4 for the given dictionary, which means it has 4 levels of nesting. 

This solution assumes that the depth of a dictionary is the maximum number of nested dictionaries it contains. If the problem is asking for the total number of nested dictionaries, the solution would be different.  For example, in the given unit test, the total number of nested dictionaries is 3, not 4.  But based on the unit test provided, the solution is correct.  If the problem is asking for the total number of nested dictionaries, the solution would be:

```
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    return 1 + sum(dict_depth(v) for v in d.values())
```

This function counts the total number of nested dictionaries by recursively going through each value in the dictionary and adding 1 to the count for each nested dictionary. The total count is the sum of the counts for all values in the dictionary.  This solution would pass the unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==3`.  However, based on the original problem statement, the first solution is correct.  The problem statement asks for the depth of a dictionary, not the total number of nested dictionaries.  The depth of a dictionary is the maximum number of nested dictionaries it contains, which is 4 in the given unit test.  The total number of nested dictionaries is 3, but that is not what the problem is asking for.  Therefore,