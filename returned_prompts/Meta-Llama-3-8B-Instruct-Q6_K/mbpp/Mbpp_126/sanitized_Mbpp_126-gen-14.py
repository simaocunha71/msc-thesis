def sum(a, b):
    a_set = set()
    b_set = set()
    for i in range(1, min(a, b) + 1):
        if a % i == 0:
            a_set.add(i)
        if b % i == 0:
            b_set.add(i)
    return sum(a_set & b_set)