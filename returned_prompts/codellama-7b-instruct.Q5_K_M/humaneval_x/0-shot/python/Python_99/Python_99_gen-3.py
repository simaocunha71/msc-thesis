
def closest_integer(value):
    if value == "0":
        return 0
    else:
        if value.find(".") != -1:
            value = value.split(".")
            value = value[0]
        value = int(value)
        if value % 2 != 0:
            return value
        else:
            if value % 10 == 0:
                return value
            else:
                return value - 1


