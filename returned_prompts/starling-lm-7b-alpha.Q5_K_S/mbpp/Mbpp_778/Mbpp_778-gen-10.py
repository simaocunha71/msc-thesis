def pack_consecutive_duplicates(l):
    result = []
    i = 0
    while i < len(l):
        start = i
        while i < len(l) - 1 and l[i] == l[i + 1]:
            i += 1
        result.append(l[start:i + 1])
        i += 1
    return result


# Test
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]






"""
Explanation:
The basic idea is to use a while loop to traverse the list. In each traversal, we find the first element that differs from the next element. We append the sublist of the current element to the result list and continue until we find the next element that differs from the current element.

In the above example,

0, 0 -> consecutive and same element, so we append [0, 0] to result
0, 1 -> not consecutive and same element, so we append [1] to result
1, 2 -> not consecutive and same element, so we append [2] to result
2, 3 -> not consecutive and same element, so we append [3] to result
3, 4 -> not consecutive and same element, so we append [4, 4] to result
4, 5 -> not consecutive and same element, so we append [5] to result
5, 6 -> consecutive and same element, so we append [6, 6, 6] to result
6, 7 -> not consecutive and same element, so we append [7] to result
7, 8 -> not consecutive and same element, so we append [8] to result
8, 9 -> not consecutive and same element, so we append [9] to result
9, 4 -> not consecutive and