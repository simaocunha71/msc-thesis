    # create a dictionary
    my_dict = {}
    for i in l:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    # loop over the dictionary
    for i in my_dict:
        if my_dict[i] > 1:
            if -i in my_dict and i != -i:
                return True
        if i == -i:
            if my_dict[i] > 1:
                return True

    return False


# Alternate Solution:
# def pairs_sum_to_zero(l):
#     """
#     pairs_sum_to_zero takes a list of integers as an input.
#     it returns True if there are two distinct elements in the list that
#     sum to zero, and False otherwise.
#     >>> pairs_sum_to_zero([1, 3, 5, 0])
#     False
#     >>> pairs_sum_to_zero([1, 3, -2, 1])
#     False
#     >>> pairs_sum_to_zero([1, 2, 3, 7])
#     False
#     >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
#     True
#     >>> pairs_sum_to_zero([1])
#     False
#     """
#     # create a dictionary
#     my_dict = {}
#     for i in l:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1

#     # loop over the dictionary
#     for i in my_dict:
#         if i == -i:
#             if my_dict[i] > 1:
#                 return True
#     for i in my_dict:
#         for j in my_dict:
#             if i != j and i + j == 0:
#                 return True
#     return False


# Alternate Solution:
# def pairs_sum_