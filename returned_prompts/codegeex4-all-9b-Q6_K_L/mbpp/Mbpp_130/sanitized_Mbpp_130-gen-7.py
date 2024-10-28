def max_occurrences(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    max_frequency = max(frequency_dict.values())
    max_items = [k for k, v in frequency_dict.items() if v == max_frequency]
    return max_items[0] if len(max_items) == 1 else max_items