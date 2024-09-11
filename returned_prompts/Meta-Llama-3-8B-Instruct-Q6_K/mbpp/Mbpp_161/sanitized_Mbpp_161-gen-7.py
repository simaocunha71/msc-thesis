def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]  # Using list comprehension to create a new list with elements not present in lst2
    # return [i for i in lst1 if i not in set(lst2)]  # Using set to remove duplicates in lst2 for better performance
    # return [i for i in lst1 if i not in lst2]  # This will also work if lst2 is a set