def get_median(list1, list2, n):
    i = 0
    j = 0
    m1 = -1
    m2 = -1

    for _ in range(n):
        if i == n:
            m1 = m2
            m2 = list2[0]
            break
        if j == n:
            m1 = m2
            m2 = list1[0]
            break

        if list1[i] <= list2[j]:
            m1 = m2
            m2 = list1[i]
            i += 1
        else:
            m1 = m2
            m2 = list2[j]
            j += 1

    return (m1 + m2) / 2

print(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5))

"""
The function first merges the two lists into one by selecting the smallest element at each step, and then it finds the median.

The time complexity is O(n), because it traverses each list once, and the space complexity is O(1), because it only uses a constant amount of space.
"""

# 2. Median of Two Sorted Arrays
