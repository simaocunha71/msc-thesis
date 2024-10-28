def consecutive_duplicates(lst):
    return list(dict.fromkeys(lst))  # Using dict.fromkeys() to remove duplicates and convert back to list