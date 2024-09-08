def max_sum_list(lst):
    max_sum = 0
    max_list = []
    for sublist in lst:
        if sum(sublist) > max_sum:
            max_sum = sum(sublist)
            max_list = sublist
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))  # Output: [10, 11, 12]

Explanation:
The function max_sum_list takes a list of lists as input. It initializes a variable max_sum to 0 and max_list to an empty list.
Then it iterates over each sublist in the input list. For each sublist, it computes the sum of its elements using the built-in sum function, and checks if this sum is greater than max_sum. If it is, the function updates max_sum to this new sum and max_list to this sublist.
Finally, the function returns the max_list.
"""

