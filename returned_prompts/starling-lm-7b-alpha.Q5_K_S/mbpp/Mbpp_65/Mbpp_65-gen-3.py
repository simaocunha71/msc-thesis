def recursive_list_sum(lst):
    sum = 0
    for i in lst:
        if type(i) == list:
            sum += recursive_list_sum(i)
        else:
            sum += i
    return sum

recursive_list_sum([1, 2, [3,4],[5,6]]) # 21


"""
def recursive_list_sum(lst):
    sum = 0
    for i in lst:
        if type(i) == list:
            sum += recursive_list_sum(i)
        else:
            sum += i
    return sum

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21
"""


"""
def recursive_list_sum(lst):
    return sum(lst) if not isinstance(lst[0], list) else sum(recursive_list_sum(i) for i in lst)

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21
"""

"""
def recursive_list_sum(lst):
    return reduce(lambda x, y: x + y, map(lambda lst: recursive_list_sum(lst), lst)) if not any(map(lambda x: isinstance(x, list), lst)) else recursive_list_sum(lst)

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21
"""

"""
def recursive_list_sum(lst):
    return reduce(lambda x, y: x + y, map(recursive_list_sum, lst)) if not any(map(lambda x: isinstance(x, list), lst)) else recursive_list_sum(lst)

assert recursive_list_sum([1, 2, [3,4],[5,6]]) == 21
"""

"""
def recursive_list_sum(lst):
    return reduce(lambda x, y: x + y, map(lambda x: recursive_list_sum(