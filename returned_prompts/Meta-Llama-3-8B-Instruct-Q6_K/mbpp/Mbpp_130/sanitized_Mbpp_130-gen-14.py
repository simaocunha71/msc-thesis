def max_occurrences(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    max_frequency = max(frequency_dict.values())
    max_items = [key for key, value in frequency_dict.items() if value == max_frequency]
    return max_items[0]