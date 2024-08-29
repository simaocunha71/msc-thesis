def sum_range_list(numbers, start_index, end_index):
    sum = 0
    for i in range(start_index, end_index+1):
        sum += numbers[i]
    return sum