def get_equal(tuples):
    lengths = [len(t) for t in tuples]
    return len(set(lengths)) == 1

print(get_equal([(11, 22, 33), (44, 55, 66)]))  # True
print(get_equal([(11, 22, 33), (44,_55)]))  # False

Explanation:
This function works by creating a list of the lengths of each tuple in the input list, then creating a set from that list. A set is a collection that only contains unique elements, so if there are two tuples of different lengths in the input list, the set will have more than one element. If there are no such tuples, the set will have only one element. So, we return True if the length of the set is 1, False otherwise.
"""

