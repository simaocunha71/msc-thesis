
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    nums.sort()
    for i in range(len(nums)-1): # add 1 to index so that they are sorted correctly
        sum = nums[i] + nums[i+1]
        if sum > 0:
            return [sum, nums[i+1]] + order_by_points([-nums[i]])
    # add 1 to index so that they are sorted correctly
    return [-nums[-1], order_by_points([-nums[0]])]

if __name__ == '__main__':
   # pass the list of numbers as command line arguments (optional)
   args = sys.argv[1:] if len(sys.argv) > 1 else []
   print order_by_points(args)