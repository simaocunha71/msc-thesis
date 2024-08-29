def square_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**2
    return sum

print(square_Sum(2))

# Output: 20

# Alternative solution
def square_Sum(n):
    return sum([i**2 for i in range(2, 2*n+1, 2)])

print(square_Sum(2))

# Output: 20

"""
In the first solution, we manually iterate through the even numbers, square them and add them to the sum.
In the second solution, we use list comprehension to accomplish the same thing in a more concise way. 
"""
<jupyter_output>
20
20
<jupyter_text>
Question 2
<jupyter_code>
