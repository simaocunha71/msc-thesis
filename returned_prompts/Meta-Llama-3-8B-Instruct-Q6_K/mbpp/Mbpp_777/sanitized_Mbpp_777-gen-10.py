def find_sum(lst):
    s = set(lst)
    sum = 0
    for i in s:
        if lst.count(i) == 1:
            sum += i
    return sum