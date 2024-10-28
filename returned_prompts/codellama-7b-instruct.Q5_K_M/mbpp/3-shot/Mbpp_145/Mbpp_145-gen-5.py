
def max_Abs_Diff(my_list):
    return max(abs(my_list[i] - my_list[j]) for i in range(len(my_list)) for j in range(i+1, len(my_list)))


