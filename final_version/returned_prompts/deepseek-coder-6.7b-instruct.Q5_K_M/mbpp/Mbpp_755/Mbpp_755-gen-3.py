def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2])) # -2


"""
Explanation:

We initialize two variables m1 and m2 to infinity. They will keep track of the smallest and the second smallest numbers.

For each number in the list, we check if it's smaller than or equal to m1. If it is, we update both m1 and m2. If it's not, we only check if it's smaller than m2. If it is, we update m2.

In the end, m2 will hold the second smallest number in the list.
"""

# Another solution
def second_smallest(numbers):
    numbers.sort()
    return numbers[1]

print(second_smallest([1, 2, -8, -2, 0, -2])) # -2

"""
Explanation:

We sort the list of numbers. The smallest number will be at index 0 and the second smallest at index 1.

We then return the number at index 1.
"""
<jupyter_output>
-2
-2
<jupyter_text>
