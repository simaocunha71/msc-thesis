def convert_list_dictionary(keys, values, scores):
    return [{key: {value: score}} for key, value, score in zip(keys, values, scores)]