"""
The general equation for a parabola is y = a(x-h)^2 + k. 
In the case of a parabola opening upwards, a is positive, so the directrix is the line y = -a*h^2. 

Here, a = 5, h = 3, and k = 2. 
Substitute these values into the equation for the directrix to find the y-intercept of the parabola.
"""

def parabola_directrix(a, h, k):
    return -a * h**2

print(parabola_directrix(5,3,2))

assert parabola_directrix(5,3,2)==-198
<jupyter_output>
-198
<jupyter_text>
Exercise 2: Write a function to find the vertex of a parabola.
<jupyter_code>
