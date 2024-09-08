def round_and_sum(lst):
    rounded_lst = [round(i) for i in lst]
    return sum(rounded_lst) * len(lst)