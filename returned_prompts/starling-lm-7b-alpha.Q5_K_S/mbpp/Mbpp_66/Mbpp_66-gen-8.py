def remove_duplicates(l):
    c = []
    for i in l:
        if i not in c:
            c.append(i)
    return c

# Testing
assert remove_duplicates([1,1,2,2,3,3]) == [1,2,3]

"""
Write a Python function to find the sum of all