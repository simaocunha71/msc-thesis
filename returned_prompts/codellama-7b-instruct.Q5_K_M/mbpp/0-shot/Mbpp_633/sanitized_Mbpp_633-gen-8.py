def pair_xor_Sum(my_list,n):
    sum = 0
    for i in range(0,len(my_list)):
        for j in range(i+1,len(my_list)):
            sum = sum + (my_list[i]^my_list[j])
    return sum