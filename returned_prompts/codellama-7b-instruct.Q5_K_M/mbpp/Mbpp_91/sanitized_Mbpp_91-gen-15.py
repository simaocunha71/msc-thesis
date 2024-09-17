def find_substring(my_list, substr):
    for word in my_list:
        if substr in word:
            return True
    return False