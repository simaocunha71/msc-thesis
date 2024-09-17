def sum_of_digits(my_list):
    return list(map(lambda x: sum(int(i) for i in str(x)), my_list))