"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def divisibleByK(k: int, listTuplesOfTupels: List[tuple]):
    """Find tuples having all their elements divisible by given k.
    :param k: The value to divide each element of the tuple with.
    :param listTuplesOfTupels: A sequence containing a collection of all the tuples in the list.
    :return: An iterable that is returned as an empty iterator when there are no elements to return and otherwise returns an element for every element divisible by k in each tuple in the list"""
    
    # The listTuplesOfTupels parameter should be a non-empty sequence containing a collection of all the tuples in the list.
    assert type(listTuplesOfTupels) is not None, "type(parameter) : not None"
    
    # Iterate over each element of tuple and increment the index counter by 1 to ensure that the iteration count does not break on an invalid input
    for index in range(0, len(listTuplesOfTupels[0]):
        if type(index) is not int or type(k) is not int:
            print("type({}) : {}".format(str(type(index)), str(type(index))), "type({}) : {}".format(str(type(k)), str(type(k))))
            return
        
        if len(listTuplesOfTupels) is not 0:
            for i, tuple in enumerate(listTuplesOfTupels):
                if type(tuple[index]) is int and type(tuple[index+1]) is int and type(tuple[index+2]) is int:
                    pass # Ignore the invalid input and continue iterating over it. The iteration count does not break on an invalid input.
            print("len({}) : {}".format(str(type(listTuplesOfTupels)), str(type(listTuplesOfTupels))))
            
            if type(tuple[index]) is int and type(tuple[index+1]) is not int: # Skip the invalid input. If a tuple has 3 elements, it would not make sense to test the last element on the fourth position.
                continue
        
        else:
            print("len