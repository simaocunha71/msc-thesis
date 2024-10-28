def unique_sublists(list_of_lists):
    list_of_tuples = {tuple(i) for i in list_of_lists}
    return {i: list_of_lists.count(i) for i in list_of_tuples}