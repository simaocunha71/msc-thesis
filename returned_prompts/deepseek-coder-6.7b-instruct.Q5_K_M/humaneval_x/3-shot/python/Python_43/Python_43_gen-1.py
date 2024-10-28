    num_set = set(l)
    for num in num_set:
        if -num in num_set:
            return True
    return False


