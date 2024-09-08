def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) # True

Explanation:
In Python, a set is a collection which is unordered and unindexed. It is written with curly brackets, and it has no duplicate elements.
By converting the list to a set, we remove any duplicates. Then we check if the length of the list and the set are equal. If they are, that means all elements in the list are unique.
"""

