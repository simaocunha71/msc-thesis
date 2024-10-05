
def can_arrange(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return i-1
    return -1

print(can_arrange([1,2,4,3,5])) # 3
print(can_arrange([1,2,3])) # -1

Explanation:

In the first example, the element at index 3 (value 3) is not greater than or equal to the preceding element (value 2). Thus, 3 is the largest index for which this condition holds true.
In the second example, all elements are in ascending order, so no such index exists. Hence, -1 is returned.
"""

# Task 2
"""
