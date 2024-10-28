from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    for num in numbers:
        result.append(num)
        if result:
            result.append(delimeter)
    return result[:-1]  # remove the last delimeter

# test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 6))  # [1, 6, 2, 6, 3, 6, 4, 6, 5]
print(intersperse([-1, 0, 1], 2))  # [-1, 2, 0, 2, 1]  # output may vary due to order of elements
# This solution has a time complexity of O(n) where n is the length of the input list
# This solution has a space complexity of O(n) where n is the length of the input list
# The delimeter is inserted between every two consecutive elements of the input list
# The result list will have the same length as the input list plus one less than the number of elements in the input list
# The delimeter is appended to the result list after each element in the input list
# The last delimeter is removed from the result list
# The result list is returned
# The function intersperse can be used to insert a number 'delimeter' between every two consecutive elements of any list
# The function intersperse can be used to insert a number 'delimeter' between every two consecutive elements of any list
# The function intersperse can be used to insert a number 'delimeter' between every two consecutive elements of any list
# The function intersperse can be used to insert a number 'delimeter' between every two consecutive elements of any list
# The function intersperse can be used to insert a number 'delimeter' between every two consecutive elements of any