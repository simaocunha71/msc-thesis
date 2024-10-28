def find_sum(lst: list) -> int:
    sum = 0
    for i in lst:
        if lst.count(i) == 1:
            sum += i
    return sum

