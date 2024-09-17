def index_minimum(my_list):
    index_min = min(range(len(my_list)), key=lambda i: my_list[i][1])
    return my_list[index_min][0]