def convert_list_dictionary(lst1,lst2,lst3):
    """
    Convert more than one list to nested dictionary
    """
    d = {}
    for i in range(len(lst1)):
        d[lst1[i]] = {}
        d[lst1[i]][lst2[i]] = lst3[i]
    return d