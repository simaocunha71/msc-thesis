def find_sum(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    sum_non_repeated = 0
    for num, frequency in frequency_dict.items():
        if frequency == 1:
            sum_non_repeated += num
    
    return sum_non_repeated