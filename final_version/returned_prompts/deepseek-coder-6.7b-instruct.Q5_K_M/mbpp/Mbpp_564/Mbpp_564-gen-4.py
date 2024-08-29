
def count_Pairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] != arr[j]:
                count += 1
    return count

print(count_Pairs([1,2,1])) # 2

Explanation:
In the given list [1, 2, 1], there are 2 pairs: (1, 2) and (1, 1). However, (1, 1) is a duplicate pair, so the function should return 2 pairs.

"""
The function works by iterating over each element in the list. For each element, it then iterates over the elements to its right in the list. If it finds a pair where the two elements are not equal, it increments the count. Finally, it returns the count.
"""

