
def convert_list_dictionary(*args):
    '''
    :param args: a list of lists, each list has the same length
    :return: a list of dictionaries, each dictionary has the same key-value pairs
    '''
    if len(args) < 1:
        return []

    if len(args[0]) != len(args[1]):
        return []

    result = []
    for i in range(len(args[0])):
        d = {}
        d[args[0][i]] = {}
        d[args[0][i]][args[1][i]] = args[2][i]
        result.append(d)
    return result


# def test_convert_list_dictionary():
#     assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
#     print(test_convert_list_dictionary())


if __name__ == '__main__':
    print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92]))
```

In this code, a function called `convert_list_dictionary` is defined, which takes in a variable number of arguments. The purpose of this function is to convert multiple lists into a nested dictionary. 

First, the function checks if there are at least one argument provided. If not, an empty list is returned. 

Next, it checks if the lengths of