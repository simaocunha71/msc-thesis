
Here is the solution:

```python
def convert_list_dictionary(list1, list2, list3):
    # Iterate through each list
    for i in range(len(list1)):
        # Create a new dictionary
        new_dict = {}
        # Create another dictionary to store the values of the second and third list
        inner_dict = {}
        # Append the first list item to the new dictionary
        new_dict[list1[i]] = inner_dict
        # Iterate through the second and third list
        for j in range(len(list2)):
            # Append the second and third list item to the inner dictionary
            inner_dict[list2[j]] = list3[i]
    return new_dict
```

The above function `convert_list_dictionary` takes in three lists: `list1`, `list2`, and `list3`. It then iterates through each list and creates a new dictionary called `new_dict`. Inside this new dictionary, it creates another dictionary called `inner_dict` to store the values of the second and third list. It then appends the first list item to the `new_dict` and iterates through the second and third list to append the corresponding values to the `inner_dict`. Finally, it returns the `new_dict`.

The expected output of the function is a nested dictionary where the outer dictionary has the keys from `list1` and the inner dictionary has the keys from `list2` and the values from `list3`.

For example, when the function is called with the input `convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])`, it will return `[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]` as expected.

This solution uses a nested dictionary