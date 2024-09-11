def list_split(lst,n):
    """
    Splits a list for every nth element, returning a list of the resulting lists.
    """
    return [lst[i::n] for i in range(n)]

# print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))


def list_split(lst,n):
    """
    Splits a list for every nth element, returning a list of the resulting lists.
    """
    return [lst[i::n] for i in range(n)]

print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))



# assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]






def list_split(lst,n):
    """
    Splits a list for every nth element, returning a list of the resulting lists.
    """
    return [lst[i::n] for i in range(n)]

# print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))



# assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f