
def lateralsurface_cone(r, h):
    import math
    l = math.sqrt(h**2 + r**2)
    return math.pi*r*l

print(lateralsurface_cone(5,12))

# 204.20352248333654
<jupyter_output>
204.20352248333654
<jupyter_text>
Problem 2:Write a function that takes in a string and returns a dictionary with each unique character in the string as the key and the number of times it appears in the string as the value.
<jupyter_code>
