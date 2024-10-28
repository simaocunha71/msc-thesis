def triangle_area(radius):
    if radius < 0:
        return None
    max_area = 0
    for a in range(1, radius):
        for b in range(a, radius):
            c = (a**2 + b**2)**0.5
            if c <= radius and a + b > c:
                area = (a*b)/2
                if area > max_area:
                    max_area = area
    return max_area