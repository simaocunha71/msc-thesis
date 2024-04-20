"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
import itertools as it
def combinations_colors(colors,length): #colors = [color]
    '''
    >>> colors_combinations(['Red','Green','Blue'],2)
     [[('Red', 'Green')], ['(Red, Blue)']]

    #combining a list of lists with a length of 3 to return the all combinations as lists of tuples.
    '''
    assert colors+colors #checks if input is correct
    n = len(colors)
    tuples_lists=[]
    for i in range(n): #for each element in the list, we make a tuple with that element and then add it to the list for all other elements.
        tuples_lists.append((colors[i],))
        
    if length==0:
        return [tuple(col) for col in combinations(tuples_lists)] #we return the generator of all tuple pairs of (col,) which can be applied to multiple elements at once. This reduces the number of tuples exponentially.
    
    else:
        if length == 1:#checking if the input is valid and generating the required output using the function length=3.
            return [[tuple(col) for col in combinations(tuples_lists)]]
        
        elif length==2: #this is just an example of how we can use this function to generate all tuples of two elements
            return list(it.combinations(tuples_lists, 2))

        else:
            raise ValueError('You have entered a non-integer value for length')