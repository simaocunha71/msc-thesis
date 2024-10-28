
def solution(lst):
    total = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            total += lst[i]
    return total

# Test
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0


# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Iterate through the list and check if the number is even and at an odd position (1-indexed). If so, add the number to the total.


# Alternative solution
def solution_alt(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution_alt([5, 8, 7, 1]) ==> 12
    solution_alt([3, 3, 3, 3, 3]) ==>9
    solution_alt([30, 13, 24, 321]) ==>0
    """

    total = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0 and i % 2 == 0:
            total += lst[i]
    return total

# Test
print(solution_alt([5, 8, 7, 1]))  # 12
print(solution_alt([3, 3, 3, 3, 3]))  # 9
print(solution_alt([30, 13, 24, 321]))  # 0

# Time complexity: O(n)
# Space complexity: O(1)

# Explanation:
# Iterate through the list and check if the number is odd and at an even position (1-indexed). If so, add the number to the total.