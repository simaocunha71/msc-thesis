"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(tuples):
    """Create the tuple of tuples from the inputted list.
    return a new tuple with all given tuples as elements.
    """
    tuples = [(x[0], x[1]) for x in tuples] # Convert each element to pair, store them into an array.
    max_product = 0 # initialize the variable 'max' which stores the maximum absolute product between numbers in pairs of two elements in a given list.
    for x in range(len(tuples)): # For every inputted tuples create another tuple with all the tuples inside it.
        current_tuple = (x[0], x[1]) # Create a new pair, store them into a variable 'currentTuple'.
        if max_product < abs(current_tuple): # If this product value is lower than the previous maximum value then update that.
            max_product = abs(current_tuple) # Set this product to be used as the final result. (Also store the current product into the max_product variable)
    return max_product