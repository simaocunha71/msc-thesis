def convert_list_dictionary(keys, values, scores):
    result = []
    for i in range(len(keys)):
        result.append({keys[i]: {values[i]: scores[i]}})
    return result