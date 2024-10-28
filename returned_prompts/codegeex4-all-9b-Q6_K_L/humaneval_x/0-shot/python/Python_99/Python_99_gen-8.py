def closest_integer(value):
    num = float(value)
    return round(num) if num % 1 <= 0.5 else round(num + 0.5)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))