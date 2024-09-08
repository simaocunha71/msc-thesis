def recursive_list_sum(input_list):
    total_sum = 0
    for element in input_list:
        if type(element) == list:
            total_sum += recursive_list_sum(element)
        else:
            total_sum += element
    return total_sum