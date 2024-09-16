def smallest_num(my_list):
    smallest = None
    for num in my_list:
        if smallest == None or num < smallest:
            smallest = num
    return smallest