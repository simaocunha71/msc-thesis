"""
def convert(x):
    r = x.real
    theta = x.imag
    if r == 0:
        return (0, 0)
    elif theta == 0:
        return (r, 0)
    else:
        return (r * math.cos(theta), r * math.sin(theta))
"""

def convert(x):
    r = abs(x)
    theta = math.atan(x.imag / x.real)
    if x.real < 0:
        theta += math.pi
    elif x.imag < 0:
        theta += 2 * math.pi
    return (r, theta)


# assert convert(1) == (1.0, 0.0)
# print(convert(1))
# print(convert(-1))
# print(convert(1j))
# print(convert(-1j))
# print(convert(1 + 1j))
# print(convert(1 - 1j))
# print(convert(-1 + 1j))
# print(convert(-1 - 1j))

```
