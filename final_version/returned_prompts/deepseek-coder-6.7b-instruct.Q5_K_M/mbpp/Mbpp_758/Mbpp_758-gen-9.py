
def unique_sublists(lst):
    count = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count:
            count[tuple_sublist] += 1
        else:
            count[tuple_sublist] = 1
    return count

# Test the function
print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

# Output: {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}



"""
