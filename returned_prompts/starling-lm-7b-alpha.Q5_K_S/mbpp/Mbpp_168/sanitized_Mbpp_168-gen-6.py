def frequency(input_list, number):
    '''This function counts the number of occurrences of a number in a given list.'''
    count = 0
    for item in input_list:
        if item == number:
            count += 1
    return count