def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def check(i):
        if i == 0:
            return True
        else:
            return arr[i] >= arr[i-1] and check(i-1)
    for i in range(len(arr)-1, -1, -1):
        if not check(i):
            return i
    return -1

# Tests
print(can_arrange([1,2,4,3,5]) == 3)
print(can_arrange([1,2,3]) == -1)
print(can_arrange([2,1,3,4,5]) == 1)
print(can_arrange([3,2,1,4,5]) == 1)
print(can_arrange([5,4,3,2,1]) == 0)
print(can_arrange([5,5,5,5,5]) == -1)