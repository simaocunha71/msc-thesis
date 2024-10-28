
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    # check if the array is empty
    if not array:
        return array

    # calculate the sum of the first and last index value
    first_index_value = array[0]
    last_index_value = array[-1]
    sum_of_first_and_last_index_value = first_index_value + last_index_value

    # check if the sum of the first and last index value is odd
    if sum_of_first_and_last_index_value % 2 == 1:
        return sorted(array)

    # check if the sum of the first and last index value is even
    if sum_of_first_and_last_index_value % 2 == 0:
        return sorted(array, reverse=True)

# test the function
print(sort_array([5]))
print(sort_array([2, 4, 3, 0, 1, 5]))
print(sort_array([2, 4, 3, 0, 1, 5, 6]))
print(sort_array([]))
print(sort_array([2, 4, 3, 0, 1, 5, 6, 6]))
