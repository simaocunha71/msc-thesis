
def total_match(lst1, lst2):
    total1 = 0
    total2 = 0
    for i in lst1:
        total1 += len(i)
    for j in lst2:
        total2 += len(j)
    if total1 < total2:
        return lst1
    elif total1 > total2:
        return lst2
    else:
        return lst1


# 2.
def make_unique(my_list):
    '''
    Write a function that takes a list and returns a new list without any duplicates.

    Examples
    make_unique([]) ➞ []
    make_unique([1, 2, 3, 2, 1]) ➞ [1, 2, 3]
    make_unique([1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 5]
    '''

    return list(set(my_list))


# 3.
def checkio(my_string):
    '''
    Write a function that takes a string as a parameter and returns True if the string is a palindrome, and False if it isn't.

    Examples
    checkio("racecar") ➞ True
    checkio("level") ➞ False
    checkio("radar") ➞ True
    '''

    if my_string == my_string[::-1]:
        return True
    else:
        return False


# 4.
def is_sorted(my_list, key=None):
    '''
    Write a function that takes a list and returns True if the list is sorted in ascending order, and False if it isn't.

    Examples
    is_sorted([]) ➞ True
    is_sorted([1]) ➞ True
    is_sorted([1, 2, 3]) ➞ True
    is_sorted([3, 2, 1]) ➞ False
    is_sorted([3, 3, 3]) ➞ True
    is_sorted([3