```
def convert_list_dictionary(keys, values, scores):
    result = []
    for i in range(len(keys)):
        temp = {keys[i]: {values[i]: scores[i]}}
        result.append(temp)
    return result
``` 

The function takes three lists as input: keys, values, and scores. It then iterates over the lists and creates a dictionary for each iteration. The dictionary has the key from the keys list as the outermost key, the value from the values list as the innermost key, and the score from the scores list as the value. The result is a list of these dictionaries. 

The unit test provided ensures that the function works correctly. For example, the input `["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]` should return ` [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]`. 

The function is then called with these inputs and the result is compared to the expected output. If the result is the same, the test passes; otherwise, it fails. This ensures that the function is working correctly. 

The function is designed to handle lists of any length, not just three. It will create a dictionary for each iteration of the loop, with the key from the keys list as the outermost key, the value from the values list as the innermost key, and the score from the scores list as the value. The result is a list of these dictionaries. 

The time complexity of the function is O(n), where n is the length of the lists. This is because the function iterates over the lists once. The space complexity is also O(n), as the function creates a new list of dictionaries. 

The function is case-sensitive and will not work correctly if the inputs contain duplicate keys. It will also not work correctly if the inputs contain non-hashable types, such as lists or dictionaries, as the keys. 

The function can be modified to handle these cases by using a different data structure, such as a pandas DataFrame, or by adding error checking code to handle these cases. 

The function is designed to be easy to read and understand, with clear and concise variable names and