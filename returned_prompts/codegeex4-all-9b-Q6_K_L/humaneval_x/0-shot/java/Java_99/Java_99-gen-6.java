def closest_integer(value):
    decimal_index = value.find('.')
    if decimal_index == -1:
        return int(value)
    else:
        decimal_part = value[decimal_index+1:]
        if decimal_part == '':
            return int(value)
        elif decimal_part[0] == '5':
            return int(value) + 1 if int(value) > 0 else int(value) - 1
        elif int(decimal_part[0]) % 2 == 1:
            return int(value) + 1 if int(value) > 0 else int(value) - 1
        else:
            return int(value)

print(closest_integer("10"))  # 10
print(closest_integer("15.3"))  # 15
print(closest_integer("14.5"))  # 15
print(closest_integer("-14.5"))  # -15
print(closest_integer("12.345"))  # 12
print(closest_integer("-12.345"))  # -12