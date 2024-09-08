def find_sum(lst):
    s = set()
    for i in lst:
        if i not in s:
            s.add(i)
    return sum(s)