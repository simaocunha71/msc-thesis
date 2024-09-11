def split_two_parts(lst, L):
    return (lst[:L], lst[L:])




"""
def split_two_parts(lst, L):
    # Create a copy of the list to avoid modifying the original
    lst_copy = lst.copy()

    # Split the list into two parts
    first_part = lst_copy[:L]
    second_part = lst_copy[L:]

    # Return the resulting lists in a tuple
    return (first_part, second_part)
"""


"""
def split_two_parts(lst, L):
    # Create a copy of the list to avoid modifying the original
    lst_copy = lst.copy()

    # Split the list into two parts
    first_part = lst_copy[:L]
    second_part = lst_copy[L:]

    # Return the resulting lists in a tuple
    return (first_part, second_part)
"""


def split_two_parts(lst, L):
    return (lst[:L], lst[L:])



split_two_parts([1,1,2,3,4,4,5,1],3)

#split_two_parts([1,2,3,4,5,6], 3)

#split_two_parts([1,2,3,4,5,6], 6)

#split_two_parts([1,2,3,4,5,6], 10)

#split_two_parts([], 10)

#split_two_parts([1], 1)

#split_two_parts([1,2,3,4,5,6], 0)

#split_two_parts([1,2,3,4,5,6], 7)

#split_two_parts([1,2,3,4,5,6], -1)

#split_two_parts([1,2,3,4,5,6], 100)

#split_two_parts([1,2,3,4,5