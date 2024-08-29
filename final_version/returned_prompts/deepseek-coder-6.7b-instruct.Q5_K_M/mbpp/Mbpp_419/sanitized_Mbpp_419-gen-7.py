def round_and_sum(lst):
    rounded = [round(num) for num in lst]
    return sum(rounded) * len(lst)