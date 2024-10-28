
def closest_integer(value):
    if value == '0':
        return 0
    if '.' in value:
        value = float(value)
        if value - int(value) == 0.5:
            return int(value) + 1
        else:
            return int(value)
    else:
        return int(value)

#   THINK ABOUT IT:
#   Is there a case you would need to test for where the value is a string?
#   Is there a case where the value is a float and not a string?
#   What do you think the "if value - int(value) == 0.5" part of the code
#   is checking?
#   How do you think you could write a similar if statement using the
#   modulo operator?
#   Can you think of a situation where you would use this function?
#   How could you use this function to simplify your code?