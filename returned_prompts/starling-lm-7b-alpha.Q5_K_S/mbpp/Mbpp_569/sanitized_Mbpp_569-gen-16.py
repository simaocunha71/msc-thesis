def sort_sublists(lists: list) -> list:
    sorted_lists = []
    for sublist in lists:
        sorted_sublist = sorted(sublist)
        sorted_lists.append(sorted_sublist)
    return sorted_lists