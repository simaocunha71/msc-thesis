"""
A parabola can be represented in the form: y = a(x - h)^2 + k
where:
    a is the vertex of the parabola (opposite the directrix)
    h is the x-coordinate of the vertex
    k is the y-coordinate of the vertex
    
The directrix, d, of a parabola can be found by the formula: d = k - a*h^2

The function can be written as follows:
"""

def parabola_directrix(a, h, k):
    return k - a * h ** 2

print(parabola_directrix(5,3,2))

# Output: -198
# This is the directrix of the given parabola.
<jupyter_output>
-198
<jupyter_text>
Question 3
<jupyter_code>
