import math
def polar_rect(radius, angle):
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    return (x, y)