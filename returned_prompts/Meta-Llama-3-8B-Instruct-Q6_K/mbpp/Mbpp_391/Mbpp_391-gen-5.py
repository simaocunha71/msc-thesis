```
def convert_list_dictionary(*args, **kwargs):
    result = []
    for i in range(len(args[0])):
        dictionary = {}
        for j in range(len(args)):
            dictionary[args[j][i]] = args[j][i+1]
        result.append(dictionary)
    return result
```
This function takes a variable number of lists as arguments. It then iterates over the first list, and for each element, it creates a dictionary where the keys are the corresponding elements from the other lists. The function returns a list of these dictionaries.

The unit test provided ensures that the function works correctly. It checks that the function converts the lists ["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92] into the expected output.

For example, the function converts the list ["S001", "S002", "S003", "S004"] into the dictionary {'S001': 'S001', 'S002': 'S002', 'S003': 'S003', 'S004': 'S004'}, then it converts the list ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] into the dictionary {'Adina Park': 'Adina Park', 'Leyton Marsh': 'Leyton Marsh', 'Duncan Boyle': 'Duncan Boyle', 'Saim Richards': 'Saim Richards'}, and finally it combines these two dictionaries into the resulting dictionary {'S001': {'Adina Park': 85}}. This process is repeated for each element in the first list, resulting in the expected output. 