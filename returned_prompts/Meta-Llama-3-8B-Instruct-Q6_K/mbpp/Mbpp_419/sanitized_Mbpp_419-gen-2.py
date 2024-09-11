def round_and_sum(lst):
    lst = [round(num) for num in lst]
    return sum(lst) * len(lst)