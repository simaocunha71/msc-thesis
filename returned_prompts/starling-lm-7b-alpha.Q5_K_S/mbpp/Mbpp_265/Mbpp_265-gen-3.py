def list_split(lst, n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

# tests
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# tests
assert list_split([1,2,3,4,5,6,7,8,9,10,11,12,13],3)==[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13]]

# tests
assert list_split([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],4)==[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

# tests
assert list_split([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],5)==[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16]]

# tests
assert list_split([],1)==[]

# tests
assert list_split([1],1)==[[1]]

# tests
assert list_split([1,2],1)==[[1], [2]]

# tests
assert list_split([1,2,3],1)==[[1], [2], [