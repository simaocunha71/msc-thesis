
def convert_list_dictionary(list1, list2, list3):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = {}
        d[list1[i]][list2[i]] = list3[i]
    return d

convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])


"""
def convert_list_dictionary(list1, list2, list3):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = {}
        d[list1[i]][list2[i]] = list3[i]
    return d

convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])
"""

# Python program to convert list to dictionary
def dict_list(list1,list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

list1 = ["S001", "S002", "S003", "S004"]
list2 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]

dict_list(list1,list2)

# Python program to convert list to dictionary
def dict_list(list1,list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d

list1 = ["S001", "S002", "S003", "S004