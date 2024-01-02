
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''

    # check if list has more than one of the same number, return
    # false.
    if len(set(lst)) < 1:
        return True
    
    # loop through list and if a number is less than or equal to 
    # another number, return false.
    for i in range(0,len(lst)):
        while (i + 1 <= len(lst) - 1):
            if lst[i] < lst[i+1]:
                return False
            
            i += 1
    
    # else, the list has only one of each number, so it is sorted.
    return True