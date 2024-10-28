```
def convert_list_dictionary(keys, values, scores):
    result = []
    for i in range(len(keys)):
        result.append({keys[i]: {values[i]: scores[i]}})
    return result
```





Solution:
```
def convert_list_dictionary(keys, values, scores):
    result = []
    for i in range(len(keys)):
        result.append({keys[i]: {values[i]: scores[i]}})
    return result
```
This function takes three lists as input: `keys`, `values`, and `scores`. It iterates over the length of `keys` and for each iteration, it creates a dictionary with the key from `keys` as the outer key and a dictionary with the value from `values` as the inner key and the score from `scores` as the value. It then appends this dictionary to the `result` list. Finally, it returns the `result` list.

The unit test provided in the question ensures that the function works correctly. It checks that the function converts the lists `["S001", "S002", "S003", "S004"]`, `["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]`, and `[85, 98, 89, 92]` to the expected output `[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]`.