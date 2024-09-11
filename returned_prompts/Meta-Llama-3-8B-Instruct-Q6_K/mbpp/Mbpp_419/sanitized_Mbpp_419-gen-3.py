def round_and_sum(lst):
    rounded_nums = [round(num) for num in lst]
    total_sum = sum(rounded_nums)
    return total_sum * len(rounded_nums)  # assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243