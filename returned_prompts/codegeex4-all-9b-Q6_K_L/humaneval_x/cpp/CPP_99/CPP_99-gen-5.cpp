def closest_integer(value):
    return int(round(float(value)))

B:
def closest_integer(value):
    return int(value)

C:
def closest_integer(value):
    return round(int(value))

D:
def closest_integer(value):
    return int(round(value))

E:
def closest_integer(value):
    return int(value) - int(value) % 2

F:
def closest_integer(value):
    return int(value) + 0.5

G:
def closest_integer(value):
    return int(round(float(value))) + 0.5

H:
def closest_integer(value):
    return int(value) + int(value) % 2

I:
def closest_integer(value):
    return int(value) - int(value) % 1.5

J:
def closest_integer(value):
    return int(value) + int(value) % 1.5
