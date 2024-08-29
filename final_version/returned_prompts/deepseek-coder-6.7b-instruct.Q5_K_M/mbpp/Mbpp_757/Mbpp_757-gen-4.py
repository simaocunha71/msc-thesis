def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))  # 2

Explanation:
The function `count_reverse_pairs` takes a list of strings as input and counts the number of pairs of strings where one string is the reverse of another. 

The outer loop iterates over each string in the list, and the inner loop iterates over each string after the current one. For each pair of strings, it checks if one string is the reverse of the other by using Python's slice notation with a step of -1. If the strings are reverse of each other, it increments the counter. 

Finally, it returns the count.
"""

# 2. Write a Python function to find the minimum number of platforms required for a railway station so that no train waits.
# Given arrival and departure times of trains in the day.

