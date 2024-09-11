def max_sum_list(input_list):
    max_sum = 0
    max_list = []
    for i in range(len(input_list)):
        if max_sum < sum(input_list[i]):
            max_sum = sum(input_list[i])
            max_list = input_list[i]
    return max_list