
def convert_list_dictionary(keys, values1, values2):
    output = []
    for i in range(len(keys)):
        temp_dict = {keys[i]: {values1[i]: values2[i]}}
        output.append(temp_dict)
    return output

keys = ["S001", "S002", "S003", "S004"]
values1 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
values2 = [85, 98, 89, 92]
print(convert_list_dictionary(keys, values1, values2))


"""
Output:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""

"""
The function `convert_list_dictionary` takes three lists as arguments: `keys`, `values1` and `values2`. It initializes an empty list named `output` to store the final result.

Then, it iterates over the `keys` list with a range of its length. For each iteration, it creates a dictionary `temp_dict` where the key is the current key from the `keys` list, and the value is another dictionary where the key is the current value from the `values1` list and the value is the corresponding value from the `values2` list.

The `temp_dict` is then appended to the `output` list.

After the loop ends, the `output` list is returned as the result.
"""

# Python code to convert more than one list to nested dictionary
def convert_list_dictionary(keys, values1, values2):
    return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]

keys = ["S001", "S002", "S003", "S004"]
values1 = ["Adina Park