def max_length(list_of_lists):
    return max((len(sublist), sublist) for sublist in list_of_lists)  # returns a tuple containing the length and the list itself