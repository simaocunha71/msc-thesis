def convert_list_dictionary(keys, values, scores):
    result = []
    for key, value, score in zip(keys, values, scores):
        result.append({key: {value: score}})
    return result