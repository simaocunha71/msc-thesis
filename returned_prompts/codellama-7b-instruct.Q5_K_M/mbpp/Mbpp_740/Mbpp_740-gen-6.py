
def tuple_to_dict(tup: tuple) -> dict:
    dic = {}
    for i in range(0, len(tup), 2):
        dic[tup[i]] = tup[i + 1]
    return dic


