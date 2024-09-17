import unittest
def sort_sublists(list_of_lists):
    for sublist in list_of_lists:
        sublist.sort()
    return list_of_lists