def tuple_intersection(tuple_list, result={}):
    for tuple in tuple_list:
        for item in tuple:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1
    return {item for item, count in result.items() if count == len(tuple_list)}


