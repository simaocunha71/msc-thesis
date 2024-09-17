def round_and_sum(num_list):
    rounded_list = [round(i) for i in num_list]
    return sum(rounded_list) * len(rounded_list)