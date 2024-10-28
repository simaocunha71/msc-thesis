def sum_even_and_even_index(my_list):
    return sum([i for i in my_list if i%2==0 and my_list.index(i)%2==0])