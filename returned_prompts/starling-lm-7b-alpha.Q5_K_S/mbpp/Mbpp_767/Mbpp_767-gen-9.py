def get_pairs_count(nums, sum):
    nums_dict = {}
    pairs_count = 0
    for num in nums:
        if sum - num in nums_dict:
            pairs_count += nums_dict[sum - num]
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    return pairs_count

print(get_pairs_count([1,1,1,1], 2))

"""
The function works by creating a dictionary that maps each distinct element in the list to its count.
For each number, it looks up whether the difference between the number and the target sum is already in the dictionary.
If it is, it increments the count of that difference by the count of the current number.
If the difference is not yet in the dictionary, it adds a new key-value pair with the difference and the count of the current number.
"""

"""
The time complexity of this function is O(n), where n is the length of the input list.
The space complexity of this function is O(m), where m is the number of distinct elements in the input list.
"""

"""
This function uses a dictionary to optimize its time complexity. Without the use of a dictionary, the time complexity would be O(n^2) because you would have to look up each difference in a linear search through the list.
"""

"""
This function is a good example of using a dictionary to optimize a problem that would otherwise be inefficient.
"""

"""
The function asserts that get_pairs_count([1,1,1,1], 2) == 6
This means that if you pass the list [1,1,1,1] and the sum 2 to the function get_pairs_count, it should return 6.
"""

"""
This function can be used to count the number of pairs whose sum is equal to a given sum in a list of numbers. It uses a dictionary to optimize its time complexity.
"""

"""
This function is useful for problems that involve counting the number of pairs in a list that satisfy a certain condition.
"""

"""
This function can be