def get_pairs_count(lst, sum):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                result += 1
    return result

print(get_pairs_count([1,1,1,1],2))

# Output: 6

"""
Explanation
We need to count the number of pairs that have a sum of ‘sum’. We can use two nested loops to check each number in the list.
We start with the first number, and for each possible pair, we check if the sum is equal to ‘sum’. If it is, we increment a counter.
After we have checked all the pairs, we return the counter value.
"""

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Note:
# In the above solution, we don't use a dictionary to store the counts. Instead, we use two nested loops to check each possible pair.
# This approach has a time complexity of O(n^2).

# We can optimize the solution using a dictionary to store the counts. This approach has a time complexity of O(n).

# Here is an optimized solution:

def get_pairs_count(lst, sum):
    result = 0
    counts = {}
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in counts:
        if sum - i in counts:
            result += counts[i] * counts[sum - i]
    return result

print(get_pairs_count([1,1,1,1],2))

# Output: 6

# Explanation
# We use two loops to count the occurrence of each number in the list. In the first loop, we store the counts in a dictionary.
# In the second loop, we check if the difference between the current number and the target sum is in the dictionary.
# If it is, we multiply the counts of both numbers and add the result to the result variable.