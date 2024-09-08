def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))  # Output: -2

"""
Explanation:
The function second_smallest takes a list of numbers as its argument.
The two variables m1 and m2 are initialized to infinity (float('inf')). 
We iterate over the elements of the list.
If the current element x is less than or equal to m1, we update m1 and m2.
If the current element x is less than m2 but not equal to m1, we update m2.
At the end, we return m2, which will be the second smallest number in the list.
"""

"""
