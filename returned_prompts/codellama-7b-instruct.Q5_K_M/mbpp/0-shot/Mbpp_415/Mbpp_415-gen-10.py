def max_Product(my_list):
    max_val = -1
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] * my_list[j] > max_val:
                max_val = my_list[i] * my_list[j]
    return (my_list[i], my_list[j])
