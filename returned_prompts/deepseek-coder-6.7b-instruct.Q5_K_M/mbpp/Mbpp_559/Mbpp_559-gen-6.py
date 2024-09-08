
def max_sub_array_sum(lst: list, n: int) -> int:
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j):
                curr_sum = curr_sum + lst[k]
            max_sum = max(max_sum, curr_sum)
    return max_sum

# Test
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))  # 7

"""
In this function, we are generating all possible sublists of the given list and finding the sum of each sublist. We then compare each sublist's sum with max_sum to find the maximum sum. 

This solution has a time complexity of O(n^3) because there are three nested loops. The space complexity is O(1) since we are not using any extra space.
"""
<jupyter_output>
7
<jupyter_text>
Kadane's AlgorithmThis algorithm improves the time complexity of the previous solution. Its complexity is O(n).
<jupyter_code>
def max_sub_array_sum(lst: list, n: int) -> int:
    max_so_far = lst[0]
    curr_max = lst[0]

    for i in range(1, n):
        curr_max = max(lst[i], curr_max + lst[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

# Test
print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))  # 7
<jupyter_output>
7
<jupyter_text>
This algorithm works by initializing two variables, max_so_far and curr_max, to the first element of the list. Then it iterates through