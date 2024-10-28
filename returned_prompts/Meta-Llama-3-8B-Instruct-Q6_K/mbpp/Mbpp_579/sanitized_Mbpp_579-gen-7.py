def find_dissimilar(test_tup1, test_tup2):
    return tuple(sorted(set(test_tup1).symmetric_difference(set(test_tup2))))
    # This code uses the set operation symmetric_difference() to find the elements that are in either set but not in both.
    # The set() function is used to convert the tuples into sets.
    # The sorted() function is used to sort the result in ascending order.
    # The tuple() function is used to convert the result back into a tuple.