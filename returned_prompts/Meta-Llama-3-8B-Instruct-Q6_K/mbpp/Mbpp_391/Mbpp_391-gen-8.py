```
def convert_list_dictionary(keys, values, scores):
    result = []
    for key, value, score in zip(keys, values, scores):
        result.append({key: {value: score}})
    return result
```
The function `convert_list_dictionary` takes three lists as input: `keys`, `values`, and `scores`. It uses the `zip` function to iterate over the three lists simultaneously. For each iteration, it creates a dictionary with the key from the `keys` list, and another dictionary with the value from the `values` list and the score from the `scores` list. The result is a list of dictionaries.

The unit test provided ensures that the function works correctly:
```
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
```
This test case checks that the function correctly converts the input lists to a list of dictionaries, as expected.