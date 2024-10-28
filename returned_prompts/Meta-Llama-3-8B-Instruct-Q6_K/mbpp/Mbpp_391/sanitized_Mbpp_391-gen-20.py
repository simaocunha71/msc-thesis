def convert_list_dictionary(*args):
    result = []
    for i in range(len(args[0])):
        temp_dict = {}
        for j in range(len(args)):
            temp_dict[args[j][i]] = args[j][i+1]
        result.append(temp_dict)
    return result