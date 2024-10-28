def max_occurrences(list):
    frequency_dict = {}
    for i in list:
        if i not in frequency_dict:
            frequency_dict[i] = 1
        else:
            frequency_dict[i] += 1
    max_occur = 0
    max_occur_num = None
    for k,v in frequency_dict.items():
        if v>max_occur:
            max_occur = v
            max_occur_num = k
    return max_occur_num
list = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]