def swap_List(l):
    l[0],l[-1]=l[-1],l[0]
    return l


#assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]












"""
def swap_List(l):
    l[0],l[-1]=l[-1],l[0]
    return l

def test():
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
test()


"""









"""
Write a Python program to create a function that takes a list of numbers and a number and returns the list of numbers with the specified number added to the end.

For example, if input is a list [1, 2, 3] and number 4, then the output should be [1, 2, 3, 4].


def append_list(l,n):
    l.append(n)
    return l

def test():
    assert append_list([1, 2, 3], 4) == [1, 2, 3, 4]
test()


"""


"""
def append_list(l,n):
    l.append(n)
    return l

def test():
    assert append_list([1, 2, 3], 4) == [1, 2, 3, 4]
test()


"""





"""
Write a Python program to create a function that takes a list and a number and returns True if the number is present in the list and False if it is not.

For example, if the input is a list [1, 2, 3, 4, 5] and the number is 3, then the output should be True. If the number is 6, then the output should be False.

def contains(l,n):
    if n in l:
        return