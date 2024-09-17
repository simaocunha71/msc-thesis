
def recursive_list_sum(lst):
    sum = 0
    for i in lst:
        if type(i) == list:
            sum += recursive_list_sum(i)
        else:
            sum += i
    return sum


