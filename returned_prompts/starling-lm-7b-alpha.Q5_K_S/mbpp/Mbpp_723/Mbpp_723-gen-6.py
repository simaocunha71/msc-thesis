def find_first(li,val):
    for i in range(len(li)):
        if li[i]==val:
            return i
    return -1

# Testing
assert find_first([1, 2, 3, 4, 5, 6, 7, 8],2)==1
assert find_first([1, 2, 3, 4, 5, 6, 7, 8],6)==6
assert find_first([],7)==-1

"""
The input is defined as two lists of the same length. Write a function