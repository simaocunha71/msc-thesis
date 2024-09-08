def convert_list_dictionary(keys, values1, values2):
    return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]