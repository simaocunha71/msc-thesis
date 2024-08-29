def count_Occurrence(tup, lst):
    count = 0
    for i in lst:
        count += tup.count(i)
    return count

# Test the function
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ))  # Output: 3


