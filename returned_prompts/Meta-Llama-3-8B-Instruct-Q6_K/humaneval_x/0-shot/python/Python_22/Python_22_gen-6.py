    # Solution
    # filter() function returns a filter object which filters the given list
    # based on the given function. 
    # The function given to filter() takes one argument and returns boolean value.
    # In this case, the function checks if the value is an integer.
    # The filter() function returns an iterator which produces values from the input list 
    # for which the function returns True. 

    # map() function applies function to every item of given list (or can be used with 
    # other iterable) and returns list of results. 
    # In this case, the function given to map() checks if the value is an integer.
    # The map() function returns an iterator which produces values from the input list 
    # for which the function returns True. 

    return list(filter(lambda x: isinstance(x, int), map(lambda x: x, values))) # Convert the iterator to a list

# Testing the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3]  # Output: [1, 2, 3