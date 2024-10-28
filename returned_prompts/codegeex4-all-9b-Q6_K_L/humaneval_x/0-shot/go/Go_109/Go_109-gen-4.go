def move_one_ball(arr):
    """
    Determine if it is possible to get an array sorted in non-decreasing order by performing the following operation on the given array:
    You are allowed to perform right shift operation any number of times.
    One right shift operation means shifting all elements of the array by one position in the right direction. The last element of the array will be moved to the starting position in the array i.e. 0th index.
    If it is possible to obtain the sorted array by performing the above operation then return true else return false.
    If the given array is empty then return true.
    Note: The given list is guaranteed to have unique elements.

    For Example:
    MoveOneBall([3, 4, 5, 1, 2])==>true
    Explanation: By performin 2 right shift operations, non-decreasing order can be achieved for the given array.
    MoveOneBall([3, 5, 4, 1, 2])==>false
    Explanation:It is not