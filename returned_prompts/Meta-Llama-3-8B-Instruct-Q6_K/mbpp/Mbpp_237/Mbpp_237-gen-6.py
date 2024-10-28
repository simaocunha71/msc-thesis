"""
def check_occurences(lst):
    result = {}
    for tup in set(map(tuple, lst)):
        result[tup] = lst.count(tup)
    return result
"""
The function `check_occurences` takes a list of tuples as input and returns a dictionary where each unique tuple is mapped to the number of times it occurs in the list. The `set` function is used to get the unique tuples, and the `map` function is used to convert the list of tuples to a set of tuples. The `count` method is then used to count the occurrences of each unique tuple in the original list. The result is a dictionary with unique tuples as keys and their counts as values.

The unit test `assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}` ensures that the function correctly returns the expected dictionary for the given input. The test checks if the function returns the expected dictionary by comparing the output with the expected output. If the output matches the expected output, the test passes; otherwise, it fails.