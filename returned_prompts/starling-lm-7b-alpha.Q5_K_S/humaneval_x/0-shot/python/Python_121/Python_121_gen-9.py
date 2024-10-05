
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.


    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum_odd = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0 and i % 2 == 0:
            sum_odd += lst[i]
    return sum_odd


# Tests
print(solution([5, 8, 7, 1]))  # 12
print(solution([3, 3, 3, 3, 3]))  # 9
print(solution([30, 13, 24, 321]))  # 0
print(solution([1, 2, 3, 4, 5]))  # 5

# Explanation
# The function solution takes a list of integers and iterates through them using a for loop.
# For each element in the list, it checks if the element is odd (by using the modulo operator % to check if the element is divisible by 2) and if the index of the element is even (by using the modulo operator % to check if the index of the element is divisible by 2).
# If both conditions are met, the element is added to the sum_odd variable.
# After iterating through all the elements in the list, the function returns the sum_odd variable, which contains the sum of all the odd elements in even positions.

# The time complexity of this solution is O(n), where n is the length of the input list, as it only iterates through the list once.
# The space complexity of this solution is O(1), as it only uses a single variable (sum_odd) to store the sum of the odd elements.

# This solution is simple and efficient, as it only requires a single pass through the list to find the odd elements in even positions, and