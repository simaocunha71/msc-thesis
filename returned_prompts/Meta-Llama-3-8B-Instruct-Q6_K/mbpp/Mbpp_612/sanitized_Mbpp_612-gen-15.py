def merge(list_of_lists):
    for sublist in list_of_lists:
        if len(sublist) != 2:
            raise ValueError("All sublists must have exactly two elements")
    first_lists = [sublist[0] for sublist in list_of_lists]
    second_lists = [sublist[1] for sublist in list_of_lists]
    return [first_lists, second_lists]