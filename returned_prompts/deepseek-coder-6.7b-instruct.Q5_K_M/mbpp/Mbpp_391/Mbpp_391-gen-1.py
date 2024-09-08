Here is the Python code to solve the problem:

```python
def convert_list_dictionary(keys, values1, values2):
    result = []
    for i in range(len(keys)):
        dict1 = {}
        dict2 = {}
        dict2[values1[i]] = values2[i]
        dict1[keys[i]] = dict2
        result.append(dict1)
    return result

print(convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]))
```

This function takes 3 lists as inputs. It iterates through the keys list and for each key, it creates a dictionary with the corresponding value from the other two lists. Then it appends this dictionary to the result list. The result list is returned as the output of the function.

The output of the function for the given example is:

```python
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
```

This is the expected output.

This solution assumes that the keys, values1, and values2 lists have the same length. If that's not the case, you'll need to add some error checking to handle that situation.
"""

