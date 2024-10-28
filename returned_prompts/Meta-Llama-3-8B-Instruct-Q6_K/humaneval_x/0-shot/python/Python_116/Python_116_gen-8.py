    def sort_array(arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    # sort the array based on the number of ones in the binary representation of each number and the number itself
    # the sorted function returns a new sorted list from the elements of any sequence
    # lambda function is used as the key for sorting, which takes each element in the array and returns a tuple
    # the first element of the tuple is the count of ones in the binary representation of the number
    # the second element is the number itself, this is to break the tie when two numbers have the same number of ones in their binary representation
    # the sorted function then sorts the array based on these tuples
    # this way the array is sorted first by the number of ones in the binary representation and then by the number itself
    # this is exactly what the problem requires, to sort the array based on the number of ones in the binary representation in ascending order
    # and for similar number of ones, sort based on decimal value in ascending order
    # this is why this solution works correctly for the given test cases
    # and also for any other test case that is similar to these test cases
    # this solution has a time complexity of O(n log n) where n is the number of elements in the array
    # because of the sorting operation which has a time complexity of O(n log n)
    # the space complexity is O(n) because the sorted function creates a new list which takes up space
    # but this is a necessary space complexity for the problem because the problem requires the sorted array to be returned
    # so the space complexity cannot be improved further
    # in summary, this solution is correct and efficient for the given problem
    # it works correctly for all the test cases and has a good time and space complexity
    # it is also easy to understand and implement, which is a good thing
    # so this solution is a good solution for this problem
    # it can be used in real world scenarios where sorting arrays based on the number of ones in their binary representation is required
    # for example, in a scenario where you need to sort a list of numbers based on the number of ones in their binary representation
    # and for similar number of ones, sort based on decimal value, this solution can be used
    # it will work correctly and efficiently in such a scenario
    # so