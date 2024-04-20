"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""
def division_elements(a, b):
    for i in range(len(a)): # for each element of a tuple
        res = a[i] / b[i]   # do the same thing for every element of a and b
        print('res', res)

# output 
# res
print()