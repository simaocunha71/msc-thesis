def convert_list_dictionary(keys, values, scores):
    result = []
    for i in range(len(keys)):
        temp = {keys[i]: {values[i]: scores[i]}}
        result.append(temp)
    return result