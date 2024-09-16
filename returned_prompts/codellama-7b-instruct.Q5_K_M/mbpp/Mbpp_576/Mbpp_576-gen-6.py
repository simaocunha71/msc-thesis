"""
def is_Sub_Array(first_array,second_array):
    if len(first_array) < len(second_array):
        return False
    for i in range(len(first_array)-len(second_array)+1):
        if first_array[i:i+len(second_array)] == second_array:
            return True
    return False
"""
