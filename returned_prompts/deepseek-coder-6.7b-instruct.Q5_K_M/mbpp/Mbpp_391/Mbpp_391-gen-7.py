"""
def convert_list_dictionary(keys, values1, values2):
    return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]

print(convert_list_dictionary(["S001",  "S002",  "S003",  "S004"],["Adina Park",  "Leyton Marsh",  "Duncan Boyle",  "Saim Richards"],[85, 98, 89, 92]))
"""

E:
"""
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""




def convert_list_dictionary(keys, values1, values2):
    return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]

print(convert_list_dictionary(["S001",  "S002",  "S003",  "S004"],["Adina Park",  "Leyton Marsh",  "Duncan Boyle",  "Saim Richards"],[85, 98, 89, 92]))

# Output:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

# The function 'convert_list_dictionary' takes three lists as input. It then creates a list of dictionaries using list comprehension. Each dictionary has a key from the 'keys' list and a value that is another dictionary with a key from the 'values1' list and a value from the 'values2' list. The index 'i' is used to access the corresponding elements from the lists. The function returns this list of dictionaries