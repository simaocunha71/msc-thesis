
def sort_even(l: list):
    # Create a list of the even indices of the original list
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    # Create a list of the values at the even indices of the original list
    even_values = [l[i] for i in even_indices]
    # Sort the list of even values
    even_values.sort()
    # Create a new list with the even values at their original indices
    new_list = [l[i] if i % 2 != 0 else even_values[i // 2] for i in range(len(l))]
    return new_list

# Testing
print(sort_even([5, 6, 3, 4]))
print(sort_even([1, 2, 3]))




def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    new_list = [l[i] if i % 2 != 0 else even_values[i // 2] for i in range(len(l))]
    return new_list

# Testing
print(sort_even([5, 6, 3, 4]))
print(sort_even([1, 2, 3]))



def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies,