
def closest_integer(value):
    return int(value) if value.count('.') == 1 and int(value) - float(value) < 0.5 else round(float(value))

# Alternate solution
# def closest_integer(value):
#     if '.' not in value:
#         return int(value)
#     integer_part, decimal_part = int(value.split('.')[0]), int(value.split('.')[1])
#     if integer_part % 2 == 0:
#         return integer_part + (decimal_part + 1) // 2
#     else:
#         return integer_part + decimal_part // 2


# Test cases
print(closest_integer("10"))  # Should return: 10
print(closest_integer("15.3"))  # Should return: 15
print(closest_integer("-14.5"))  # Should return: -15
print(closest_integer("14.5"))  # Should return: 15
print(closest_integer("10."))  # Should return: 10
print(closest_integer("10.5"))  # Should return: 11
print(closest_integer("-10.5"))  # Should return: -11
print(closest_integer("-10."))  # Should return: -10


















































































































































































