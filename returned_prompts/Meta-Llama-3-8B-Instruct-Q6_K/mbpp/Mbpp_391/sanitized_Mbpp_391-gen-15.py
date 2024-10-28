def convert_list_dictionary(*args, **kwargs):
    result = []
    for i in range(len(args[0])):
        dictionary = {}
        for j in range(len(args)):
            dictionary[args[j][i]] = args[j][i+1]
        result.append(dictionary)
    return result