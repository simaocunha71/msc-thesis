
def tuple_to_dict(t):
    result = {}
    for i in range(0, len(t)-1, 2):
        result[t[i]] = t[i+1]
    return result


