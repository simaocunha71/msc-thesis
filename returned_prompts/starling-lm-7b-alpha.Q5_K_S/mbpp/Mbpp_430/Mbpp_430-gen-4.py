def parabola_directrix(a, h, k):
    d = -1 / (4 * a)
    return d * (h ** 2) + k

# assert parabola_directrix(5,3,2)==-198

def parabola_directrix(a, h, k):
    d = -1 / (4 * a)
    return d * (h ** 2) + k

# assert parabola_directrix(5,3,2)==-198

"""
def parabola_directrix(a, h, k):
    d = -1 / (4 * a)
    return d * (h ** 2) + k
"""

# Testing
print(parabola_directrix(5,3,2)) # -198




# Here is some helpful information about the problem that you might find useful:
# The equation of a parabola is given by y = ax^2 + bx + c. Here a, b, and c are constants. We can write the equation of a parabola in vertex form as follows:
# y = a(x - h)^2 + k, where h is the x-coordinate of the vertex and k is the y-coordinate of the vertex. The vertex of the parabola is the point (h, k) on the graph.
# The axis of symmetry of a parabola is a vertical line that passes through the vertex. The equation of the axis of symmetry is x = h.
# The directrix of a parabola is a horizontal line that is equidistant from the vertex and the focus of the parabola. The equation of the directrix is y = k - p, where p is the distance from the vertex to the focus.
# In the vertex form of the equation of a parabola, the y-coordinate of the vertex (k) is equal to the distance from the vertex to the focus, and the x-coordinate of the vertex (h) is equal to the x-coordinate of the point where the parabola intersects the axis of symmetry.
# The distance from the vertex to the focus of a parabola is given by the formula p = 1 / (4a),