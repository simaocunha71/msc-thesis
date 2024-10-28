def min_val(lst):
    lst = [int(x) if type(x) == str and x.isdigit() else x for x in lst]
    try:
        return min(lst)
    except ValueError:
        return "Error: The list contains a string that cannot be converted to an integer."