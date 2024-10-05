def closest_integer(value):
    value = float(value)
    return round(value) if value >= 0 else round(value) - 1

print(closest_integer("10"))  # 10
print(closest_integer("15.3"))  # 15
print(closest_integer("14.5"))  # 15
print(closest_integer("-14.5"))  # -15