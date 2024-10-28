
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_index = [i for i in range(len(l)) if i % 2 == 0]
    odd_index = [i for i in range(len(l)) if i % 2 != 0]
    even_l = [l[i] for i in even_index]
    odd_l = [l[i] for i in odd_index]
    return odd_l + sorted(even_l)


# Created by: Madeline
# Date: May 17, 2021
# This program is for Codewars' Python Katas

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_index = [i for i in range(len(l)) if i % 2 == 0]
    odd_index = [i for i in range(len(l)) if i % 2 != 0]
    even_l = [l[i] for i in even_index]
    odd_l = [l[i] for i in odd_index]
    return odd_l + sorted(even_l)

# Made By: Madeline
# Date: May 1