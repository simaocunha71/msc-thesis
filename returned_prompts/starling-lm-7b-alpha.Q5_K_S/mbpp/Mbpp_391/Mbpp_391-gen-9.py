from collections import defaultdict

def convert_list_dictionary(s_list, name_list, score_list):
    d = defaultdict(dict)
    for i in range(len(s_list)):
        d[s_list[i]][name_list[i]] = score_list[i]
    return [d]

# assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

"""
The above code will fail if the length of the three lists are not same
"""

# To handle the case when the lists have unequal lengths, the following code can be used

def convert_list_dictionary(s_list, name_list, score_list):
    d = defaultdict(dict)
    for i in range(len(s_list)):
        d[s_list[i]][name_list[i]] = score_list[i] if i < len(name_list) and i < len(score_list) else None
    return [d]

# assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, None])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': None}]



"""
If you want to use a single dictionary instead of a list