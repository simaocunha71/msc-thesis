def merge(test_list: list) -> list:
    result = [[], []]
    for sublist in test_list:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result

