def frequency_lists(test_list):
    result = {}
    for sublist in test_list:
        for item in sublist:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result

