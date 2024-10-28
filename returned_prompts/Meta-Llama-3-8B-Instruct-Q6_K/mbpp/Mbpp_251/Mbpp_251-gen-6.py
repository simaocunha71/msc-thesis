def insert_element(lst, elem):
    result = [elem] + lst + [elem]
    return result

assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']  # test case
print(insert_element(['Red', 'Green', 'Black'] ,'c')) # test case
print(insert_element([1,2,3], 0)) # test case
print(insert_element(['a', 'b', 'c'], 'd')) # test case
print(insert_element([], 'x')) # test case
print(insert_element(['x'], 'y')) # test case
print(insert_element(['x'], '')) # test case
print(insert_element(['x'], None)) # test case
print(insert_element(['x'], '')) # test case
print(insert_element(['x'], [])) # test case
print(insert_element(['x'], {})) # test case
print(insert_element(['x'], {'a':1})) # test case
print(insert_element(['x'], {'a':1, 'b':2})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4, 'e':5})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8})) # test case
print(insert_element(['x'], {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9})) #