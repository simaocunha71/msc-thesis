
Here is a Python function that converts a given list of lists to a nested dictionary:

```python
def convert_list_dictionary(list_1, list_2, list_3):
    """Converts a given list of lists to a nested dictionary."""
    # Assuming each list has equal length
    assert len(list_1) == len(list_2) == len(list_3)

    result = {}
    for index, item in enumerate(list_1):
        result[item] = {}
        result[item][list_2[index]] = list_3[index]

    return result
```

You can test the function with the provided example:

```python
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
```

The function works by creating an empty dictionary and then iterating over the input lists. For each iteration, it assigns the current item from `list_1` as the key in the result dictionary. It then creates a new dictionary as the value for this key and assigns the current item from `list_2` as the key in this new dictionary. Finally, it assigns the current item from `list_3` as the value for this key. This process is repeated for each iteration, resulting in a nested dictionary with the desired structure.

Please note that this function assumes that the input lists have the same length. If the lists have different lengths, you will need to modify the function to handle this situation.

It's worth mentioning that the assertion `assert len(list_1) == len(list_2) == len(list_3)` is used to check if all the input lists have the same length. If they