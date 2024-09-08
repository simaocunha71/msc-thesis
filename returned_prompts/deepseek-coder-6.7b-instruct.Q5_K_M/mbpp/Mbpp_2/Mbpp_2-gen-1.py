
def similar_elements(l1, l2):
    return set(l1) & set(l2)

print(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)))

assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""

