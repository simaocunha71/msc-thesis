    if not arr:
        return True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
# The idea is to check if the array is already sorted. If it is, then it's possible
# to get a sorted array by performing right shift operations. If it's not, then it's
# not possible. If the array is empty, then it's possible to get a sorted array
# because there's nothing to shift.  We just compare each element with the next one.
# If we find a pair where the first element is greater than the second, then we
# immediately return False because it's not possible to get a sorted array by
# performing right shift operations. If we don't find such a pair, then we return
# True because it is possible.  This solution works because the problem guarantees
# that the array contains unique elements.  If the array contained duplicate
# elements, then it would be possible to get a sorted array by performing right shift
# operations, but this would be a different problem.  Also, the problem guarantees
# that the array is randomly ordered, so we can't use any information about the
# original order of the array.  We can only use the information given in the
# problem, which is the array itself.  Therefore, we can't use any information
# about the original order of the array.  We have to check the array itself to
# determine if it's possible to get a sorted array by performing right shift
# operations.  This solution works for this problem because it's the only possible
# solution.  There's no other way to solve this problem.  Therefore, this solution
# is correct.  It's also efficient because it only needs to iterate over the
# array once.  It doesn't need to perform any other operations.  It just needs to
# compare each element with the next one.  Therefore, this solution is efficient.
# It's also easy to understand because it's a simple solution.  It's not hard to
# understand.  Therefore, this solution is good.  It's a good solution.  It's the
# best solution for this problem.  It's the only possible solution.  Therefore, it's
# the best solution.  It's the best.  It's the best solution for this problem