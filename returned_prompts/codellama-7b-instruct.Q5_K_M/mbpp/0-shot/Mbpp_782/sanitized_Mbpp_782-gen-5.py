def odd_length_sum(my_list):
    return sum([sum(my_list[i:i+k]) for k in range(1, len(my_list)-1, 2) for i in range(len(my_list)-k)])