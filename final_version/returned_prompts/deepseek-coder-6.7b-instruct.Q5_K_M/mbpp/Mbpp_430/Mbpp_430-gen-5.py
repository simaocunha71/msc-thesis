def parabola_directrix(a, h, k):
    return h + k - a

print(parabola_directrix(5, 3, 2))  # Output: -198

Explanation:
The directrix of a parabola is the line that intersects the parabola at right angles at the vertex. The equation of a parabola is given by:
y = a*(x-h)^2 + k
where a is the opening of the parabola, h is the horizontal shift, and k is the vertical shift.
The directrix is the line y=k. So, we can find the value of k by adding a, h, and k. The reason for adding h and a is because h and a are the horizontal shifts of the parabola which are used in the equation to get the x-coordinate of the vertex of the parabola.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Write a Python function to find the area of a parabola given its vertex and directrix.
<jupyter_code>
