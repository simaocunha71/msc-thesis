def closest_integer(value):
    if value.count(".") == 1:
        if value[-1] >= "5":
            return int(value[:-2]) + 1 if value[0] != "-" else int(value[:-2]) - 1
        return int(value[:-2])
    return int(value)

print(closest_integer("14.5"))
print(closest_integer("-14.5"))
print(closest_integer("10"))
print(closest_integer("15.3"))