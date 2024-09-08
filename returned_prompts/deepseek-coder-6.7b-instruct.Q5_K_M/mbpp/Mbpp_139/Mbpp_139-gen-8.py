def circle_circumference(radius):
    return 2 * math.pi * radius

print(math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001))

"""
In this function, we use the formula for the circumference of a circle, which is 2πr (where r is the radius of the circle). 
We then return the result. The 'math.isclose' function checks if the result of our function matches the expected result within a specified tolerance.
"""
<jupyter_output>
True
<jupyter_text>
Question 3
<jupyter_code>
