```
def convert_list_dictionary(keys, values, scores):
    result = []
    for key, value, score in zip(keys, values, scores):
        result.append({key: {value: score}})
    return result
```


This function takes three lists: keys, values, and scores. It then uses the zip function to iterate over these lists in parallel. For each iteration, it creates a dictionary with the key from the keys list, and another dictionary with the value from the values list and the score from the scores list. This new dictionary is then added to the result list. The function finally returns the result list. The unit test provided ensures that this function works correctly. 

For example, if the input lists are ["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92], the function will return [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]. 