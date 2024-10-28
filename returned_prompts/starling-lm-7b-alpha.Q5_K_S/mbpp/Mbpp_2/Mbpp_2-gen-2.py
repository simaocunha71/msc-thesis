"""
def similar_elements(list1, list2):
    return list(set(list1) & set(list2))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
print("All tests passed")

"""

def similar_elements(list1, list2):
    return list(set(list1) & set(list2))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
print("All tests passed")






def similar_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
print("All tests passed")










def similar_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
print("All tests passed")





def similar_elements(list1, list2):
    return list(set(list1) & set(list2))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
print("All tests passed")




def similar_elements(list1, list2):
    return list(set(list1).intersection(set(list2)))

# Testing the code
assert set(similar_elements((3, 4, 5, 6),(5, 7,