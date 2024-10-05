
def double_the_difference(lst):
    lst = lst[::-1]
    sum = 0
    for i in range(len(lst)):
        if (lst[i] % 2 != 0) and (lst[i] > 0):
            sum = sum + lst[i]
            if i != len(lst) - 1:
                sum = sum + lst[i+1]
    return sum
