def min_val(lst):
    num_list = [num for num in lst if isinstance(num, (int, float))]
    if num_list:
        return min(num_list)
    else:
        return None  # or some other default value