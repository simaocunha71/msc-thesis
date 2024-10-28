def two_unique_nums(num_list):
    # Convert list to set to remove duplicate numbers
    num_set = set(num_list)
    # Convert set back to list
    num_list = list(num_set)
    return num_list