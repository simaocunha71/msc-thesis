def odd_length_sum(my_list):
    sum = 0
    for i in range(1, len(my_list)):
        for j in range(i+1, len(my_list)):
            if j-i+1%2==1:
                sum += my_list[i] + my_list[j]
    return sum