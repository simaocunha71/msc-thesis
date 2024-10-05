
def sort_array(array):
    # sort array in ascending order
    array.sort()
    # sum first and last value of array
    sum_first_last = array[0] + array[-1]
    # if sum of first and last value is odd
    if sum_first_last % 2 != 0:
        # return the sorted array
        return array
    # else if sum of first and last value is even
    else:
        # return the sorted array in descending order
        return array[::-1]

