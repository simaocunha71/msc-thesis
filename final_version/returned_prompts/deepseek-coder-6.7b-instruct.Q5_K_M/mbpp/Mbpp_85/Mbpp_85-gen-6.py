
import math

def surfacearea_sphere(radius):
    surfacearea = 4 * math.pi * radius ** 2
    return surfacearea

print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))
<jupyter_output>
True
<jupyter_text>
Question 2:
<jupyter_code>
