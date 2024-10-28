def round_and_sum(lst):
    rounded_sum = sum(round(num) for num in lst)
    return rounded_sum * len(lst)