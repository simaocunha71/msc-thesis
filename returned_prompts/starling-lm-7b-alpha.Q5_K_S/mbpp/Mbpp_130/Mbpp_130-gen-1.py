```
def max_occurrences(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_num = None
    max_count = 0
    for num, count in counts.items():
        if count > max_count:
            max_num = num
            max_count = count

    return max_num
```

Explanation:
We first create a dictionary called `counts` to store the frequency of each number in the list. We iterate through the input list and for each number, if it already exists in the `counts` dictionary, we increment its count by 1. Otherwise, we add the number to the dictionary and set its count to 1. After we finish iterating through the list, we iterate through the `counts` dictionary to find the number with maximum count. We initialize `max_num` and `max_count` to None and 0 respectively, and update them if we find a number with a higher count. Finally, we return the number with maximum count as the result.

This solution has a time complexity of O(n), where n is the length of the input list, as we only iterate through the list once and the dictionary. The space complexity is also O(n) as we store the frequency of each number in the dictionary.

The provided assert statement is a test case for the `max_occurrences` function, checking if it correctly identifies the number with maximum frequency in the given list. The expected output is 2, as the number 2 appears 5 times in the list, which is the maximum frequency among all numbers in the list.

You can use this function by calling `max_occurrences` with a list of integers as the argument. It will return the number with maximum frequency in the list.

Note that the function assumes that the input list does not contain duplicate numbers with the same value, but different frequencies. If the list may contain such duplicate numbers, you may need to modify the function accordingly to handle them.

Additionally, if you need to find