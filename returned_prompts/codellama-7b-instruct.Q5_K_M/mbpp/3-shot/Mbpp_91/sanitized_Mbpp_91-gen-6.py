def find_substring(my_list, substr):
    return any(substr in s for s in my_list)