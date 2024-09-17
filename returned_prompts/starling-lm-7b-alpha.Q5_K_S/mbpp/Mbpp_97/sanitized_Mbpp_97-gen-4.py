def frequency_lists(list_of_lists):
    dictionary = {}
    for item in list_of_lists:
        for i in item:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary