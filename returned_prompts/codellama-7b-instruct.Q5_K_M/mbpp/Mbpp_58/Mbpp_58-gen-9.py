def opposite_Signs(a,b):
    return (a < 0 and b > 0) or (a > 0 and b < 0)

# OR

def opposite_Signs(a,b):
    return (a * b) < 0

# OR

def opposite_Signs(a,b):
    return a * b < 0

# OR

def opposite_Signs(a,b):
    return a < 0 and b > 0 or a > 0 and b < 0

# OR

def opposite_Signs(a,b):
    return (a - b) == (-1) or (a - b) == 1

# OR

def opposite_Signs(a,b):
    return abs(a) + abs(b) == -1 or abs(a) + abs(b) == 1

# OR

def opposite_Signs(a,b):
    return a + b == -1 or a + b == 1

# OR

def opposite_Signs(a,b):
    return (a - b) == -1 or (a - b) == 1

# OR

def opposite_Signs(a,b):
    return a == -b

# OR

def opposite_Signs(a,b):
    return a + b == -1 or a + b == 1
