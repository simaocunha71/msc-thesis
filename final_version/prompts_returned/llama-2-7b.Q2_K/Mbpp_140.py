"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(list_of_lists):
    result = []

    for items in list_of_lists:
        for item in items:
            if not isinstance(item, list):
                result.append(item)
            else:
                if len(result) > 0 and type(result[-1]) == str:
                    result = []
                result.extend(item)
    return result
    

print(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]))