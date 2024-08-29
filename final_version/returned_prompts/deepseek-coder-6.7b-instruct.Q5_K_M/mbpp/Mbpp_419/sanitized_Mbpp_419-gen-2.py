def round_and_sum(lst):
    rounded_lst = [round(num) for num in lst]
    return sum(rounded_lst) * len(lst)