
def compare_one(a, b):
    if type(a) != type(b):
        if a == b:
            return None
        elif a.isdigit() and b.isdigit():
            if float(a) == float(b):
                return None
            elif float(a) < float(b):
                return a
            else:
                return b
        elif a.replace(',', '') == b.replace(',', ''):
            if float(a.replace(',', '')) == float(b.replace(',', '')):
                return None
            elif float(a.replace(',', '')) < float(b.replace(',', '')):
                return a.replace(',', '')
            else:
                return b.replace(',', '')
        else:
            if b.replace(',', '') < a.replace(',', ''):
                return b.replace(',', '')
            else:
                return a.replace(',', '')
    else:
        if a == b:
            return None
        elif a < b:
            return a
        else:
            return b
```

Explanation:
This solution defines a function called `compare_one` that takes in two parameters, `a` and `b`. The function checks if the types of `a` and `b` are different. If they are different, it further checks if both `a` and `b` are integers or floats. If they are, it converts `a` and `b` to floats and compares them. If `a` is less than `b`, it returns `a`. If `b` is less than `a`, it returns `b`. If `a` and `b` are equal, it returns `None`. 

If `a` and `b` are not integers or floats, the function checks if they are both strings with commas as the decimal separator. If they are, it removes the commas from `a` and `b` and converts them to floats. It then compares the floats and returns the larger value or `None` if they are equal. 

If `a` and `b` are not