def convert_list_dictionary(lst1,lst2,lst3):
    """
    Convert more than one list to nested dictionary
    """
    d = {}
    for i in range(len(lst1)):
        d[lst1[i]] = {}
        d[lst1[i]][lst2[i]] = lst3[i]
    return d



# assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
# print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]))


# Here is a Python function to convert the given lists to a nested dictionary:

def convert_list_dictionary(lst1,lst2,lst3):
    """
    Convert more than one list to nested dictionary
    """
    d = {}
    for i in range(len(lst1)):
        d[lst1[i]] = {}
        d[lst1[i]][lst2[i]] = lst3[i]
    return d
```
        
Here's how you can use the function to convert the given lists to a nested dictionary:

```python
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85,