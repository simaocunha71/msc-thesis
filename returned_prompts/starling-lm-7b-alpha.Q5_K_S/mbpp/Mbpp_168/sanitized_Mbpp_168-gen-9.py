def frequency(lst, num):
    '''This function counts the number of occurrences of a number in a list.'''
    count = 0
    for i in lst:
        if i == num:
            count += 1
    return count