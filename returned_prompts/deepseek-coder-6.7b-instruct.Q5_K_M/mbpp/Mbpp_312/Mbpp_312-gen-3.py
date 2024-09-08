
def volume_cone(radius, height):
    return (1/3) * math.pi * (radius**2) * height

# Testing the function
print(math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001))
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
