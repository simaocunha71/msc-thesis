"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""
def split_two_parts(list_, L):
    first, second = [] ,[]
    for i in range (0, len(list_), L):
        second.append(list_.pop(i))
    return [first,second]