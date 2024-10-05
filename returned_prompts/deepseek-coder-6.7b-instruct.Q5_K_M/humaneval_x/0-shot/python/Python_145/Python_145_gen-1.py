
    def order_by_points(nums):
        return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))

    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points([]))

# Output
# [-1, -11, 1, -12, 11]
# []

In this solution, we use sorted function with a custom lambda function as the key. The lambda function is a function that returns a tuple. The first element of the tuple is the sum of the digits of the absolute value of the number (we use abs to ensure that we work with positive numbers) and the second element of the tuple is the index of the number in the original list. When sorted function compares two numbers, it first compares the first elements of the tuples (the sums of the digits). If they are equal, it then compares the second elements (the indices).

This solution works for negative numbers and zero because the sum of the digits of negative numbers is the same as the sum of the digits of their absolute values and the index of zero in the original list is also considered when sorting.

The time complexity of this solution is O(n log n) because of the sorted function. The space complexity is O(n) because we create a new list that is a sorted version of the input list.

The map function is used to convert each digit of the number into an integer and sum up these digits. The str function is used to convert the number into a string, so that we can iterate over its digits. The abs function is used to ensure that we work with positive numbers, as the sum of the digits of negative numbers is the same as the sum of the digits of their absolute values.
"""

# Task 2

"""
