def find_even_pair(L):
    c = 0
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            if (L[i]^L[j])%2 == 0:
                c += 1
    return c




"""
The above solution will have a time complexity of O(n^2). This can be optimized by using a hash map.

def find_even_pair(L):
    c = 0
    d = {}
    for i in L:
        if i in d:
            d[i] = not d[i]
            if d[i]:
                c += 1
        else:
            d[i] = True
    return c
"""

# def find_even_pair(L):
#     c = 0
#     for i in range(len(L)):
#         for j in range(i+1, len(L)):
#             if (L[i]^L[j])%2 == 0:
#                 c += 1
#     return c


find_even_pair([5, 4, 7, 2, 1])
#find_even_pair([1,2,3,4,5])
#find_even_pair([1,2,3,4,5,6,7])
#find_even_pair([1,2,3,4,5,6,7,8])
#find_even_pair([1,2,3,4,5,6,7,8,9])

# find_even_pair([3, 2, 5, 3, 4, 1, 7, 3, 6, 3, 8, 3, 9, 3, 3, 3, 3, 3, 3, 3, 3])
#find_even_pair([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2