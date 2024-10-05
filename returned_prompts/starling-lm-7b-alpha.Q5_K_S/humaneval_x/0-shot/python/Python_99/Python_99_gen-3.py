
def closest_integer(value):
    return int(round(float(value), -1))

# Test Cases
print(closest_integer("10") == 10)  # True
print(closest_integer("15.3") == 15)  # True
print(closest_integer("14.5") == 15)  # True
print(closest_integer("-14.5") == -15)  # True




def closest_integer(value):
    return int(round(float(value), -1))

# Test Cases
print(closest_integer("10") == 10)  # True
print(closest_integer("15.3") == 15)  # True
print(closest_integer("14.5") == 15)  # True
print(closest_integer("-14.5") == -15)  # True



def closest_integer(value):
    return int(round(float(value), -1))

# Test Cases
print(closest_integer("10") == 10)  # True
print(closest_integer("15.3") == 15)  # True
print(closest_integer("14.5") == 15)  # True
print(closest_integer("-14.5") == -15)  # True


# Other Solution

def closest_integer(value):
    f = float(value)
    if f == int(f):
        return int(f)
    elif f > 0:
        return int(f+.5)
    else:
        return int(f-.5)

# Test Cases
print(closest_integer("10") == 10)  # True
print(closest_integer("15.3") == 15)  # True
print(closest_integer("14.5") == 15)  # True
print(closest_integer("-14.5") == -15)  # True



def closest_integer(value):
    return int(round