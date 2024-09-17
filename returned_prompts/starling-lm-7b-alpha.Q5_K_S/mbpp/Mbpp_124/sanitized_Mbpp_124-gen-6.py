import math
import numpy as np
def angle_complex(x, y):
    angle = np.arctan(y/x)
    phase = np.angle(x + y * 1j)
    
    # Adjust the angle if it's outside the range of -π/2 to π/2
    if angle < -math.pi/2:
        angle += 2 * math.pi
    elif angle > math.pi/2:
        angle -= 2 * math.pi
    
    return angle