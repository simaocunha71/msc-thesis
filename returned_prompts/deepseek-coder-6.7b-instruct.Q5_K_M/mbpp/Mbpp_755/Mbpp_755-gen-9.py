def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for n in numbers:
        if n <= m1:
            m1, m2 = n, m1
        elif n < m2:
            m2 = n
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

#Output: -2

#Explanation: The smallest number is -8 and the second smallest number is -2. So, -2 is returned.

"""
The function works by initializing two variables m1 and m2 to positive infinity.

It then iterates through the list of numbers. If it encounters a number n that is less than or equal to m1, 
it updates m1 and m2 to be n and the previous value of m1 respectively. If it encounters a number n that is 
greater than m1 but less than m2, it updates m2 to be n.

After it has iterated through all the numbers, m2 will hold the second smallest number in the list.
"""
<jupyter_output>
-2
<jupyter_text>
Find the Second Largest Number in a List
<jupyter_code>
