def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]  # using list comprehension with built-in sorted function