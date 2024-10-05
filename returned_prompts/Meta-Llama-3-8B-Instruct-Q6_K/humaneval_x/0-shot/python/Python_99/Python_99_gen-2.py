```
def closest_integer(value):
    value = float(value)
    if value % 1 == 0:
        return int(value)
    elif value > 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)
```



This function works by first converting the input string to a float. It then checks if the float is already an integer (i.e., if the decimal part is 0). If it is, it simply converts the float to an integer and returns it. If the float is not an integer, it checks if the float is positive. If it is, it adds 0.5 to the float and converts it to an integer. If the float is negative, it subtracts 0.5 from the float and converts it to an integer. This ensures that the function rounds away from zero when the float is equidistant from two integers. For example, `closest_integer("14.5")` will return `15`, and `closest_integer("-14.5")` will return `-15`.