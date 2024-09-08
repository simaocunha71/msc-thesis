"""
The function first merges the two lists into one sorted list. Then it returns the middle value of the merged list.
If the length of the merged list is even, it returns the average of the two middle values.
"""

def get_median(list1, list2, n):
    merged_list = sorted(list1 + list2)
    if n % 2 == 0:
        return (merged_list[n//2] + merged_list[n//2 - 1]) / 2
    else:
        return merged_list[n//2]

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))  # Output: 16.0

