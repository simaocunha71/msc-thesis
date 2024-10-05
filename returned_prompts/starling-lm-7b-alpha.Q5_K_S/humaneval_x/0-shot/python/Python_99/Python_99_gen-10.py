
def closest_integer(value):
    x = int(value[:value.find('.')])
    y = int(value[:value.find('.')]) + 1
    if abs(x - float(value)) <= abs(y - float(value)):
        return x
    else:
        return y

# Test cases
print(closest_integer("10"))      # 10
print(closest_integer("15.3"))    # 15
print(closest_integer("-14.5"))   # -15
print(closest_integer("14.5"))    # 15


# Other solutions

def closest_integer(value):
    return int(round(float(value) + 0.5) - 0.5)

# Test cases
print(closest_integer("10"))      # 10
print(closest_integer("15.3"))    # 15
print(closest_integer("-14.5"))   # -15
print(closest_