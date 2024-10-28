def convert_list_dictionary(a, b, c):
    result = []
    for i in range(len(a)):
        temp = {a[i]: {b[i]: c[i]}}
        result.append(temp)
    return result