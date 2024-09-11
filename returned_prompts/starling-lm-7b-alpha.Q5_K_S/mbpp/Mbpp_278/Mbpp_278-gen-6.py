from collections import defaultdict
def count_first_elements(tuples):
    d = defaultdict(int)
    for t in tuples:
        if isinstance(t, tuple):
            d[t[0]] += 1
        else:
            d[t] += 1
    return sum(d.values())

# Alternatively, we can use Counter from collections to simplify this function
from collections import Counter
def count_first_elements(tuples):
    d = Counter()
    for t in tuples:
        if isinstance(t, tuple):
            d[t[0]] += 1
        else:
            d[t] += 1
    return sum(d.values())

# Testing
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
# count_first_elements((1, (1, 2), (1, 2, 3)) ) == 2
# count_first_elements((1, (1, 2, 3), (1, 2)) ) == 3
# count_first_elements((1, 2, (1, 2), 3) ) == 2

# With Counter
# assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
# count_first_elements((1, (1, 2), (1, 2, 3)) ) == 2
# count_first_elements((1, (1, 2, 3), (1, 2)) ) == 3
# count_first_elements((1, 2, (1, 2), 3) ) == 2


"""
This function first creates a defaultdict to store the counts of each element in the tuple. It then iterates through the tuples, checking if the element is a tuple itself. If it is, it increments the count of the first element in the tuple. If it's not, it increments the count of the element itself. Finally, it returns the sum of all the counts in the defaultdict.

The alternative solution uses Counter from the collections module, which is a