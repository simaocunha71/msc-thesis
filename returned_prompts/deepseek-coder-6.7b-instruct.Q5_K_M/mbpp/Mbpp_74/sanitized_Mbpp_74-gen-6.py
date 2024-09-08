def is_samepatterns(color_array, pattern_array):
    color_dict = {}
    pattern_dict = {}

    for i in range(len(color_array)):
        if color_array[i] not in color_dict:
            color_dict[color_array[i]] = [i]
        else:
            color_dict[color_array[i]].append(i)

    for i in range(len(pattern_array)):
        if pattern_array[i] not in pattern_dict:
            pattern_dict[pattern_array[i]] = [i]
        else:
            pattern_dict[pattern_array[i]].append(i)

    color_values = list(color_dict.values())
    pattern_values = list(pattern_dict.values())

    return color_values == pattern_values