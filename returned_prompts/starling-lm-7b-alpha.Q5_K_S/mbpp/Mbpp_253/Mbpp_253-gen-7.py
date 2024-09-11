"""
def count_integer(list):
    integer_list = []
    for i in range(len(list)):
        if isinstance(list[i], int):
            integer_list.append(list[i])
    return len(integer_list)

assert count_integer([1,2,'abc',1.2]) == 2
"""

