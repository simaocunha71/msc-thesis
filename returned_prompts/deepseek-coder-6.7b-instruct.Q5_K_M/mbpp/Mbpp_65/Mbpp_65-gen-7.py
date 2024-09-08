
def recursive_list_sum(lst):
    sum = 0
    for i in lst:
        if type(i) == list:
            sum += recursive_list_sum(i)
        else:
            sum += i
    return sum

print(recursive_list_sum([1, 2, [3,4],[5,6]])) # Output: 21



