
import cmath
def convert(num):
    mod = abs(num)
    angle = cmath.phase(num)
    return (mod, angle)


