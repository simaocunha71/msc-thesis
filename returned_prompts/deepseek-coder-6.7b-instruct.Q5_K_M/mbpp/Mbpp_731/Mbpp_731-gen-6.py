import math
def lateralsurface_cone(r, h):
    return math.pi * r * math.sqrt(r**2 + h**2)

print(lateralsurface_cone(5,12))

#assert lateralsurface_cone(5,12)==204.20352248333654
<jupyter_output>
204.20352248333654
<jupyter_text>
Problem 3
<jupyter_code>
