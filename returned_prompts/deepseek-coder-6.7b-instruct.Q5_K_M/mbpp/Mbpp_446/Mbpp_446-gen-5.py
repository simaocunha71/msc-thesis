def count_Occurrence(tuple_in, list_in):
    count = 0
    for i in list_in:
        count += tuple_in.count(i)
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] )) # Should print 3


