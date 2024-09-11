"""
def swap_List(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp
    return input_list

#Test the function
assert(swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12])
"""

def swap_List(input_list):
    temp = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = temp
    return input_list

#Test the function
assert(swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12])


