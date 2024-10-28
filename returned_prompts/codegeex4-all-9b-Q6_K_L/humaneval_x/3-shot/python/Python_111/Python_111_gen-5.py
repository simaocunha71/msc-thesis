    count_dict = {}
    result = {}

    for c in test:
        if c not in count_dict:
            count_dict[c] = 1
        else:
            count_dict[c] += 1

    if not count_dict:
        return result

    max_count = max(count_dict.values())
    for k, v in count_dict.items():
        if v == max_count:
            result[k] = v

    return result

