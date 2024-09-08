def test_duplicate(lst):
    return len(lst) != len(set(lst))

print(test_duplicate([1,2,3,4,5])) # False
print(test_duplicate([1,2,3,4,2])) # True
"""

