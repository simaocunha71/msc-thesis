def move_zero(lst):
    # create an empty list to store the zeroes
    zeroes = []
    # create an empty list to store the non-zeroes
    non_zeroes = []
    # loop through the list
    for elem in lst:
        # if the element is zero, append it to the zeroes list
        if elem == 0:
            zeroes.append(elem)
        # otherwise, append it to the non-zeroes list
        else:
            non_zeroes.append(elem)
    # concatenate the zeroes and non-zeroes lists
    return non_zeroes + zeroes


# Test
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]


"""
In this solution, we create two empty lists: one to store the zeroes and one to store the non-zeroes. We then loop through the input list, checking each element. If the element is zero, we add it to the zeroes list; otherwise, we add it to the non-zeroes list. Finally, we concatenate the zeroes and non-zeroes lists and return the result. This ensures that all the zeroes are moved to the end of the list while preserving the original order of the non-zeroes.
"""

"""
In this solution, we first create a new list called 'non_zero_list' and a variable called 'i' to keep track of the index. We then loop through the input list. If the current element is not zero, we append it to the 'non_zero_list' and increment 'i' by 1. If the current element is zero, we append the next element from the 'non_zero_list' (if it exists) to the current position in the input list, and then append the zero to the end of the list. After the loop, we return the modified input list. This ensures that all the zeroes are moved to the end of the list while preserving the original order of the non-zeroes.
"""

"""
In this solution, we use the built-in 'filter' function to create a new list that only contains the non-zero elements from the input list. We then use the 'extend' method