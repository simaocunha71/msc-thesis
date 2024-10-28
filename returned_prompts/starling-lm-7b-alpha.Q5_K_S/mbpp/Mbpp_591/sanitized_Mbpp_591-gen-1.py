def swap_List(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp
    return input_list