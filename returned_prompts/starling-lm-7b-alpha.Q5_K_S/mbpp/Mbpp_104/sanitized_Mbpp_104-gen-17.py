def sort_sublists(sublists):
    sorted_sublists = []
    for sublist in sublists:
        sorted_sublist = sorted(sublist)
        sorted_sublists.append(sorted_sublist)
    return sorted_sublists