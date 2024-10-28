def sort_numeric_strings(my_list):
    return sorted(my_list, key=lambda s: [int(x) if x.isdigit() else x for x in s.split()])