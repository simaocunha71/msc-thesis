"""
def get_median(a, b):
    if len(a) == 0:
        return b[len(b) // 2]
    if len(b) == 0:
        return a[len(a) // 2]
    if len(a) > len(b):
        return get_median(b, a)
    if len(a) == 1:
        return (a[0] + b[len(b) // 2]) / 2.0
    if len(b) == 1:
        return (b[0] + a[len(a) // 2]) / 2.0
    if len(a) % 2 == 0:
        return (a[len(a) // 2] + a[len(a) // 2 - 1] + b[len(b) // 2]) / 3.0
    if len(b) % 2 == 0:
        return (b[len(b) // 2] + b[len(b) // 2 - 1] + a[len(a) // 2]) / 3.0
    if a[len(a) // 2] < b[len(b) // 2]:
        return a[len(a) // 2] + (b[len(b) // 2] - a[len(a) // 2]) / 2.0
    else:
        return b[len(b) // 2] + (a[len(a) // 2] - b[len(b) // 2]) / 2.0
"""

def get_median(a, b):
    if len(a) == 0:
        return b[len(b) // 2]
    if len(b) == 0:
        return a[len(a) // 2]
    if len(a) > len(b):
        return get_median(b, a)
    if len(a) == 1:
        return (a[0] + b[len(b) // 2]) / 2.0
    if len(b) == 1: