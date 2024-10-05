```
def compare_one(a, b):
    if type(a) == float and type(b) == float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == str and type(b) == str:
        a = a.replace(",", ".")
        b = b.replace(",", ".")
        if float(a) > float(b):
            return a
        elif float(a) < float(b):
            return b
        else:
            return None
    elif type(a) == float and type(b) == str:
        a = a
        b = float(b.replace(",", "."))
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == str and type(b) == float:
        a = float(a.replace(",", "."))
        b = b
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    else:
        return None
```



This function compares the two given values. It first checks if both values are of the same type. If they are floats, it compares them directly. If they are strings, it converts them to floats by replacing the commas with dots, and then compares them. If the values are of different types, it converts the non-float value to a float and then compares them. If the values are equal, it returns None. If the values are of different types and cannot be compared (for example, a float and a string), it returns None.