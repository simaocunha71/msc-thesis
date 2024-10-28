import cmath
def polar_rect(r: float, theta: float) -> (complex, complex):
    return (r * cmath.rect(1, theta), r * cmath.rect(1, theta + math.pi / 2))