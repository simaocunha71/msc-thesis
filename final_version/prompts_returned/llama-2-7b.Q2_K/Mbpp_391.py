"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""

def convert_list_dictionary(a, b, c):
    # create a temporary list of the first parameter.
    d = []

    for element in a:
        if isinstance(element, str):
            d.append({str(element):b[0]})
        else:
            raise Exception("Can't append element type to dictionary. ")

    return d
