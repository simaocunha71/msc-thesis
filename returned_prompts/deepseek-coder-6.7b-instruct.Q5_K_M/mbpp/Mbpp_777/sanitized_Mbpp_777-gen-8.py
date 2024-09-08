def find_sum(lst):
    non_repeated = set()
    for num in lst:
        if lst.count(num) == 1:
            non_repeated.add(num)
    return sum(non_repeated)