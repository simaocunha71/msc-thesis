def find_sum(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    sum = 0
    for num, freq in freq_dict.items():
        if freq == 1:
            sum += num
    
    return sum