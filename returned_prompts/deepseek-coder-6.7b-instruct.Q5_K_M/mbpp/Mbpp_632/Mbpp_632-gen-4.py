def move_zero(lst):
    # Create two lists, one for non-zero values and one for zero values
    non_zero = [i for i in lst if i != 0]
    zero = [i for i in lst if i == 0]
    # Combine the two lists and return the result
    return non_zero + zero

print(move_zero([1,0,2,0,3,4]))  # [1,2,3,4,0,0]




"""
