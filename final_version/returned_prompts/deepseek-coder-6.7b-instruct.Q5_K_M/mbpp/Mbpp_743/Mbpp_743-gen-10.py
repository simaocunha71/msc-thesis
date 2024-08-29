def rotate_right(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

# Output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

"""
Explanation:
In the function, we are using Python's slicing to rotate the list. We are taking the last k elements and adding it to the front of the list, and then adding the remaining elements in the list to the end. 
So, if we have a list [1,2,3,4,5] and we want to rotate it 2 times to the right, it becomes [4,5,1,2,3].
"""

# Solution 2:
def rotate_right(lst, k):
    res = [0] * len(lst)
    for i in range(len(lst)):
        res[(i + k) % len(lst)] = lst[i]
    return res

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

# Output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

"""
Explanation:
In this solution, we're creating a new list of the same length as the original list filled with zeros. Then we iterate over the original list, and for each element at index i, we put it in the new list at index (i + k) % len(lst). This is equivalent to rotating the list to the right by k places. The % operator is used to ensure that if k is larger than the length of the list, we only rotate by k % len(lst) places.
"""

# Solution 3:
def rotate_right(lst, k):
    return [lst[i - k] for i in range(len(lst))]
