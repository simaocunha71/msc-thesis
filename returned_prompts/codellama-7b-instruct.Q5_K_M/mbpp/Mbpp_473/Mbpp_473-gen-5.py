def tuple_intersection(tuple_list, result={}):
    if not tuple_list:
        return result
    else:
        current_tuple = tuple_list.pop()
        for item in current_tuple:
            if item not in result:
                result[item] = current_tuple
        return tuple_intersection(tuple_list, result)

def tuple_intersection(tuple_list):
    return tuple(tuple_intersection(tuple_list, {}).values())

# 1
def tuple_intersection(tuple_list):
    return tuple(set.intersection(*map(set, tuple_list)))

# 2
import collections
def tuple_intersection(tuple_list):
    return tuple(collections.Counter(sum(tuple_list, ())).keys())
