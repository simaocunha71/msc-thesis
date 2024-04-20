"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""
def rear_extract(tuples):
    """
    :param tuples: the list containing the tuples to extract from.
    
    :return tuple: The list of tuples which are extracted from the input tuples.
    """
    new_list = []
    for item in range(len(tuples)): # Going through each iteration and extracting the rear element from each tuple.
        temp_list = [(t[1], t[2])]
        del tuples[-1]
        new_list += list(map(lambda x: (x, x[0]))(temp_list)) # Adding the rear elements to a separate list.
    return new_list