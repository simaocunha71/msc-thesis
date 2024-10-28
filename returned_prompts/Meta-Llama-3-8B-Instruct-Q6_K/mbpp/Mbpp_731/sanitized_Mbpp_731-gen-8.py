import math
def lateralsurface_cone(r, h):
    return math.pi * r * (r + math.sqrt((h**2) + (r**2)))  # Calculate the lateral surface area of a cone
    # return math.pi * r * (r + math.sqrt(h**2 + r**2))  # Alternative formula for calculating the lateral surface area of a cone