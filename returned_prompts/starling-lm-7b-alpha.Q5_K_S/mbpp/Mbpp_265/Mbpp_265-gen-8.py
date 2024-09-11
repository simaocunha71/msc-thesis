def list_split(input_list, n):
    return [input_list[i::n] for i in range(n)]



# Assert
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# Test
print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3))  # [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
print(list_split(['a', 'b', 'c', 'd', 'e'],2))  # [['a', 'c'], ['b', 'd', 'e']]
print(list_split(['a', 'b'],1))  # [['a'], ['b']]


# Explain
The function returns a list of lists, where every nth element is in a new list.
For example, for input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], n = 3,
the resulting list is [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']].


"""

"""

# Code

def list_split(input_list, n):
    return [input_list[i::n] for i in range(n)]

# Assert
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k