def closest_integer(value):
    if "." in value:
        number = float(value)
        if number > 0:
            return int(number) if number - int(number) < 0.5 else int(number) + 1
        else:
            return int(number) if abs(number - int(number)) < 0.5 else int(number) - 1
    else:
        return int(value)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))