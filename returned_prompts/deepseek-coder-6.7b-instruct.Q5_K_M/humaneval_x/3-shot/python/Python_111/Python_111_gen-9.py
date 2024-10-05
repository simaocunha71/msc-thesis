    count_dict = {}
    words = test.split(' ')
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    max_value = max(count_dict.values()) if count_dict else 0
    return {k: v for k, v in count_dict.items() if v == max_value}


