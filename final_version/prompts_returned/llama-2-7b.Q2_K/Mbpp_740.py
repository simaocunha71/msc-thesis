"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. 
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
from typing import *
def tuple_to_dict(tuple_list:Tuple):
	"""Convert a tuple to dictionary using adjacent elements."""
	my_dictionary = {}
    for element in tuple_list:
        if not element in my_dictionary.keys():
            my_dictionary[element] = element
        elif type(element) == int or float :
            try:
                my_dictionary[element] += 1
            except TypeError as error:
                print("Error in key: ", element, ' in dictionary: ', my_dictionary )
        else:
            raise ValueError('Value of a non-number is not allowed')
    return my_dictionary
    
    

if __name__ == "__main__":
	print(tuple_to_dict((1, 5, 7, 10, 13, 5)))