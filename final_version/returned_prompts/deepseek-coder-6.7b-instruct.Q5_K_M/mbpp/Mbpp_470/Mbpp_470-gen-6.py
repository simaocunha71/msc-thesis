
def add_pairwise(tup):
    return tuple([tup[i] + tup[i+1] for i in range(len(tup)-1)])

print(add_pairwise((1, 5, 7, 8, 10)))

# Output:
# (6, 12, 15, 18)

# Explanation:
# The pairwise addition of the neighboring elements of the given tuple (1, 5, 7, 8, 10) is (5+7, 7+8, 8+10) = (12, 15, 18).

# Solution 2:

