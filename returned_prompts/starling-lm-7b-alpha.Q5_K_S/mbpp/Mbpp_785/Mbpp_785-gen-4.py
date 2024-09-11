def tuple_str_int(t):
    s = t.split(',')
    return tuple(map(int, s))

# assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)


# Python3 program to convert list to tuple
# Python program to convert list to tuple

def list_to_tuple(li):
    return tuple(li)

# Driver Code

if __name__=="__main__":
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_to_tuple(li))

"""
Output:
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
"""

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10)


# Python3 program to convert tuple to list
# Python program to convert tuple to list

def tuple_to_list(tu):
    return list(tu)

# Driver Code

if __name__=="__main__":
    tu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tuple_to_list(tu))

"""
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10)


# Python3 program to convert list of tuples to a
# dictionary with tuple's first element as key

def tuple_list_to_dict(li):
    d = {}
    for tup in li:
        d[tup[0]] = tup[1]
    return d

# Driver Code

if __name__=="__main__":
    li = [('a', 2), ('b', 3), ('c', 4)]
    print(tuple