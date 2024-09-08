def round_and_sum(lst):
    sum = 0
    for num in lst:
        sum += round(num)
    return sum * len(lst)