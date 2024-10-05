    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    max_value = -1
    for num, freq in frequency_dict.items():
        if freq >= num and num > max_value:
            max_value = num

    return max_value

