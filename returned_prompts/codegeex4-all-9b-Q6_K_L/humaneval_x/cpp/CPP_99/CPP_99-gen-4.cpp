def closest_integer(value):
    x = float(value)
    if x >= 0:
        return round(x + 0.5)
    else:
        return round(x - 0.5)

B:
def closest_integer(value):
    x = float(value)
    if x >= 0:
        return round(x)
    else:
        return round(x - 1)

C:
def closest_integer(value):
    x = float(value)
    if x >= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)

D:
def closest_integer(value):
    x = float(value)
    if x >= 0:
        return round(x + 1)
    else:
        return round(x - 1)

E:
def closest_integer(value):
    x = float(value)
    if x >= 0:
        return int(x + 1)
    else:
        return int(x - 1)

F:
def closest_integer(value):
    x = float(value)
    if x >= 0:
        return round(x)
    else:
        return round(x + 1)
