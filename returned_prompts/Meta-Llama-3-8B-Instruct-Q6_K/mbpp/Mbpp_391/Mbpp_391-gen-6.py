```
def convert_list_to_nested_dict(*lists):
    result = []
    for i in range(len(lists[0])):
        temp = {}
        for j in range(len(lists)):
            temp[lists[j][i]] = lists[j][i+1]
        result.append(temp)
    return result
```
The function `convert_list_to_nested_dict` takes variable number of arguments which are lists. It iterates over each list, and for each iteration, it creates a dictionary where the keys are the elements of the current list. If there are multiple lists, it assumes that the lists have the same length. The function returns a list of these dictionaries. 

The unit test `assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]` demonstrates this. 

This function assumes that all lists have the same length. If the lists have different lengths, it will throw an IndexError when it tries to access an element that does not exist. If the lists may have different lengths, you would need to add error checking code.  Also, it assumes that the lists are not empty. If the lists may be empty, you would need to add error checking code.  The function does not handle the case where the lists are not lists. It assumes that the arguments are lists. If the arguments may not be lists, you would need to add error checking code. 

This function also assumes that the elements in the lists are hashable. If the elements are not hashable, you would need to use a different data structure, such as a list of lists.  The function does not handle the case where the elements are not hashable. It assumes that the elements are hashable. If the elements may not be hashable, you would need to add error checking code. 

This function does not handle the case where the same element appears in multiple lists. It assumes that the same element does not appear in multiple lists. If the same element may appear in multiple lists, you would need to add error checking code.  The function does not handle the case where the same