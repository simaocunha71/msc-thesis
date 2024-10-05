def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False


print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True

# Explanation:
# If we sequentially apply the operations, the balance will be as follows:
# 1 (+) -> 2 (+) -> 5 (+) -> 4 (-) -> 0 (-4)
# The balance never falls below zero, so the function should return False.
#
# If we now apply the operation [-4], the balance will be as follows:
# 0 (-4) -> -4 (-)
# The balance falls below zero, so the function should return True.

# Complexity Analysis:
# The time complexity of this function is O(n), where n is the length of the operations list. This is because we perform a single iteration over the operations list.
# The space complexity is O(1), as we only use a single variable to keep track of the balance, regardless of the size of the operations list.
# This makes it a very efficient solution.

# This code is written in Python 3.7.3.
# If you have any questions or need further clarification, feel free to ask.

# Code by Sagar Sutar
# GitHub: https://github.com/sagarsutar
# LinkedIn: https://www.linkedin.com/in/sagarsutar/
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2**Given an array of integers, find the maximum sum of a subsequence with the constraint that no two elements in the selected numbers in the subsequence should be adjacent in the given array.Example:**Input**: [1, 2, 9, 4, 5, 0, 4, 11, 6]**Output**: 26**Explanation**: The subsequence with maximum sum is [1, 9, 5, 11].
<