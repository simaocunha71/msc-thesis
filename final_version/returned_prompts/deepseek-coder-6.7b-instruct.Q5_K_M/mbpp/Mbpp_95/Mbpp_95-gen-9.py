
def Find_Min_Length(lst):
    min_len = len(lst[0])
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
    return min_len

print(Find_Min_Length([[1], [1, 2]]))  # Output: 1

"""
Explanation:
The function Find_Min_Length takes a list of lists as input. It first sets the minimum length to the length of the first list. Then, it iterates through the list of lists, checking the length of each sublist. If it finds a sublist with a smaller length than the current minimum length, it updates the minimum length. Finally, it returns the smallest length found.
"""

# Q2:
"""
Write a Python function that takes a list of numbers and returns a new list with the elements in reverse order.
assert Reverse_List([1,2,3,4]) == [4,3,2,1]
"""

A2:

def Reverse_List(lst):
    return lst[::-1]

print(Reverse_List([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

"""
Explanation:
The function Reverse_List takes a list as input. It uses Python's slicing feature to create a new list that starts from the end of the input list and ends at the beginning, stepping backwards by one element at a time. The result is a new list that has the same elements as the input list, but in reverse order.
"""

# Q3:
"""
Write a Python function that takes a list of numbers and a number n, and returns a new list that contains every nth element from the original list. 
assert Every_Nth([1,2,3,4,5,6,7,8,9,10], 2) == [2, 4, 6, 8, 10]
"""

A3:

def Every_Nth(lst, n):
    return lst[n-1::n]

print(Every_