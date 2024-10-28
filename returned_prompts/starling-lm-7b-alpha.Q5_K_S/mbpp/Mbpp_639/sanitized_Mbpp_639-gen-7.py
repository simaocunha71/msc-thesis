def sample_nam(name_list):
    total_length = 0
    for name in name_list:
        if name[0] != 'd' and name[0] != 'D':
            total_length += len(name)
    return total_length