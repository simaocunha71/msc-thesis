def convert_list_dictionary(*args):
    '''
    :param args: a list of lists, each list has the same length
    :return: a list of dictionaries, each dictionary has the same key-value pairs
    '''
    if len(args) < 1:
        return []

    if len(args[0]) != len(args[1]):
        return []

    result = []
    for i in range(len(args[0])):
        d = {}
        d[args[0][i]] = {}
        d[args[0][i]][args[1][i]] = args[2][i]
        result.append(d)
    return result