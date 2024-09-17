```
def convert_list_dictionary(keys, values, scores):
    result = []
    for key, value, score in zip(keys, values, scores):
        result.append({key: {value: score}})
    return result
```
The provided function `convert_list_dictionary` takes three lists as input: `keys`, `values`, and `scores`. It then uses the `zip` function to iterate over the three lists simultaneously, and for each iteration, it creates a dictionary with a single key-value pair. The key is taken from the `keys` list, the value is taken from the `values` list, and the score is taken from the `scores` list. This dictionary is then appended to the `result` list. Finally, the function returns the `result` list.

For example, if we call `convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])`, the output will be `[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]`. This is a list of dictionaries, where each dictionary has a single key-value pair. The key is taken from the `keys` list, and the value is a dictionary with a single key-value pair. The key in the inner dictionary is taken from the `values` list, and the value is taken from the `scores` list. This is a common use case for converting multiple lists to a nested dictionary.