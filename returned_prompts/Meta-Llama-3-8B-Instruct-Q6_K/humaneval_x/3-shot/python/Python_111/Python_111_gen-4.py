    if not test:
        return {}
    
    test_list = test.split()
    max_count = 0
    max_dict = {}
    
    for char in set(test_list):
        count = test_list.count(char)
        if count > max_count:
            max_count = count
            max_dict = {char: count}
        elif count == max_count:
            max_dict[char] = count
    
    return max_dict


