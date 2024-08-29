def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Output: -2
# The second smallest number in the list is -2.

"""
Explanation:
The function second_smallest takes a list of numbers as input. It first initializes two variables, m1 and m2, to positive infinity. It then iterates over each number in the list. If the number is smaller than or equal to m1, it updates m1 and m2 with the number and the previous value of m1. If the number is in between m1 and m2 and is not equal to m1, it updates m2 with the number. The function finally returns the value of m2 which is the second smallest number in the list.
"""

# END SOLUTION
<jupyter_output>
-2
<jupyter_text>
3. Write a Python program to sort a list of tuples using Lambda.
<jupyter_code>
# START SOLUTION

