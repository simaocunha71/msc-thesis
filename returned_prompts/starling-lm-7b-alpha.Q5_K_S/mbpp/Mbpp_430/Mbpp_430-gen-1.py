"""
The equation of a parabola in standard form is y = ax^2 + bx + c. The directrix of this parabola is y = k, where k is the value of the equation when x = p, where p is the vertex of the parabola. The vertex of the parabola is (h, k), where h = -b/(2a) and k = c - h^2.

Here, a = 5, b = 3, and c = 2. Plugging these values into the equation for the vertex, we get:

h = -3/(2*5) = -3/10
k = 2 - (-3/10)^2 = 2 - 9/100 = 198/10

So the directrix is at the point (-3/10, 198/10). To find the equation of the parabola's directrix, we can plug in the x-coordinate of the vertex into the equation of the parabola:

y = 5*(-3/10)^2 + 3*(-3/10) + 2 = 9/10 - 9/10 + 2 = 2

So the directrix of the parabola is y = 2.
"""

def parabola_directrix(a,b,c):
    h = -b/(2*a)
    k = c - h**2
    return k

# Test the function
assert parabola_directrix(5,3,2)==-198

# More tests
print(parabola_directrix(1,-2,3)) # 2
print(parabola_directrix(2,3,1)) # 1/2
print(parabola_directrix(1,0,1)) # 0
print(parabola_directrix(2,1,2)) # 3/4
print(parabola_directrix(1,1,2)) # 1

```
1
2
3
4
5

The directrix of a parabola with the equation $y = ax^2 + bx + c$ is $k$, where