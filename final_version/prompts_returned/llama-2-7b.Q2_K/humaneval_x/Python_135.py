
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # This is the most basic way of doing this sort of things
    # It is O(n log n) time complexity with a best case of O(n) and worst
    # case of O(n log n).
    def helper(i, j, k):
        if k > i:
            if arr[j] < arr[k]:
                return helper(j+1, i-1, -1)
        elif j == 0 and k==1:
            return i
        else:
            return helper(i, j-1, k-1)
    return helper(-1, arr.index(min(arr)), max(arr))
