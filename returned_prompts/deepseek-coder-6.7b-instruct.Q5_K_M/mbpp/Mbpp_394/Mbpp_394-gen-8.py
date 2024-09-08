def check_distinct(tup):
    return len(tup) == len(set(tup))

print(check_distinct((1, 4, 5, 6, 1, 4)))  # False
"""
The function works by converting the tuple to a set. A set is an unordered collection of unique elements.
If the length of the set is equal to the length of the tuple, there were no duplicates.
"""

"""
The other approach is to use a Counter object from the collections module.

def check_distinct(tup):
    return all(v == 1 for v in collections.Counter(tup).values())
"""

"""
The collections.Counter(tup).values() method returns a list of the counts of each unique object in the tuple.
The all() function returns True if all elements in the iterable are true (or if the iterable is empty).
In this case, if all counts are 1, then all elements in the tuple are unique.
"""

"""
Another approach is to sort the tuple and check for adjacent elements being equal.

def check_distinct(tup):
    return all(x != y for x, y in zip(sorted(tup), tup[1:]))
"""

"""
The zip() function makes an iterator that aggregates elements from each of the iterables.
The sorted() function returns a sorted list from the elements in the tuple.
If any two adjacent elements in the sorted list are equal, then the elements in the tuple were not unique.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:Write a function that returns the number of unique elements in a tuple.
<jupyter_code>
def count_unique(tup):
    return len(set(tup))

print(count_unique((1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8, 9, 9)))  # 9
<jupyter_output>
9
<jupyter_text>
Q3:Write a function