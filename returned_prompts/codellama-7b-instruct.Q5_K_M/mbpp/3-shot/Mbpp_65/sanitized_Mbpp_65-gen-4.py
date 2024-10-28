def recursive_list_sum(my_list):
    sum = 0
    for element in my_list:
        if isinstance(element, list):
            sum += recursive_list_sum(element)
        else:
            sum += element
    return sum