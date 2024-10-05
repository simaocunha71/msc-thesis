    if not test:
        return {}

    test_list = test.split()
    max_count = 0
    max_count_dict = {}

    for letter in test_list:
        if letter in max_count_dict:
            max_count_dict[letter] += 1
        else:
            max_count_dict[letter] = 1

        if max_count_dict[letter] > max_count:
            max_count = max_count_dict[letter]
            max_count_dict = {letter: max_count_dict[letter]}

    return max_count_dict


