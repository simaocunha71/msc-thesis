def kth_element(arr, k):
    return sorted(arr)[k - 1]


# assert kth_element([12,3,5,7,19], 2) == 3


def main():
    arr = [12,3,5,7,19]
    k = 2
    print(kth_element(arr, k))


if __name__ == "__main__":
    main()


"""
The solution is a simple function that sorts the given array and returns the kth element. In Python, indexing starts at 0, but the problem asks for 1-based indexing, so the result array is off by one.
"""

"""
The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(1) because it only uses a small amount of extra memory.
"""

"""
The solution works by using Python's built-in sorted function, which returns a new list that is a sorted version of the input list. The kth element is then accessed using k - 1, since indexing starts at 0. This is a simple and efficient solution to the problem.
"""

"""
The solution assumes that the input array is non-empty and that k is a valid index into the array (i.e., k is between 1 and the length of the array, inclusive). If these assumptions are not met, the solution may raise an error.
"""

"""
The solution does not handle cases where k is greater than the length of the array. If k is greater than the length of the array, the solution will raise an IndexError when trying to access the kth element of the sorted array. To handle this case, you can add a check to ensure that k is within the valid range before calling the kth_element function.
"""

"""
The solution can be easily modified to handle cases where the input array is empty or when k is less than 1. You can add a check at the beginning of the function to handle these cases.
"""

"""
The solution can also be modified to handle cases where the input array contains duplicate elements. In such cases, the kth element can be any element that appears k times in the array. To find such an element,