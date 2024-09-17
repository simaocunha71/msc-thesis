
def find_sum(my_list: list) -> int:
    result = 0
    for i in my_list:
        if my_list.count(i) == 1:
            result += i
    return result


