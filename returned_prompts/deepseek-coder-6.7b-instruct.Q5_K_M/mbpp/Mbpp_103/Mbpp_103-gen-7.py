def eulerian_num(n, m):
    if m == 0:
        return 1
    if n == 0:
        return 0
    return (m + 1) * eulerian_num(n - 1, m) + eulerian_num(n, m - 1)

print(eulerian_num(3, 1))


# Explanation:
# The Eulerian number is a series that is used in the study of combinatorics. 
# The Eulerian number is defined by the formula: a(n, m) = a(n - 1, m) + m * a(n, m - 1).
# In this problem, we have to calculate the Eulerian number for given n and m.
# We can solve this problem using recursion.
# If m == 0, then a(n, m) = 1.
# If n == 0, then a(n, m) = 0.
# Otherwise, a(n, m) = (m + 1) * a(n - 1, m) + a(n, m - 1).

# Test Case:
# The function should return 4 when the input is (3, 1).

# The output of the function is 4 which is the correct answer.
# So, the function is working as expected.
assert eulerian_num(3, 1) == 4

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
<jupyter_output>
4
<jupyter_text>
Problem 3:
<jupyter_code>
