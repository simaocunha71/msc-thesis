def extract_singly(lists):
    result = set()
    for lst in lists:
        result.update(lst)
    return result
"""
This function takes a list of lists as input and returns a set of unique numbers.
The function iterates over each list in the input list of lists, and uses the update method of the set to add the elements of the list to the set.
The set data structure automatically removes any duplicate elements, so the function can return a set of unique numbers.
The function also uses the set comprehension syntax, which is a concise way to create a set from an iterable.
"""



