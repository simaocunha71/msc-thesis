
def compare_one(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif isinstance(a, str) and a.replace(",","").isdigit():
        if float(a.replace(",","")) > float(b.replace(",","")):
            return a
        elif float(b.replace(",","")) > float(a.replace(",","")):
            return b
        else:
            return None
    elif isinstance(b, str) and b.replace(",","").isdigit():
        if float(b.replace(",","")) > float(a.replace(",","")):
            return b
        elif float(a.replace(",","")) > float(b.replace(",","")):
            return a
        else:
            return None
    elif isinstance(a, str) and a.replace(".", "", 1).isdigit():
        if float(a.replace(".","", 1).replace(",","")) > float(b.replace(",","")):
            return a
        elif float(b.replace(",","")) > float(a.replace(".","", 1).replace(",","")):
            return b
        else:
            return None
    elif isinstance(b, str) and b.replace(".", "", 1).isdigit():
        if float(b.replace(".","", 1).replace(",","")) > float(a.replace(".","", 1).replace(",","")):
            return b
        elif float(a.replace(".","", 1).replace(",","")) > float(b.replace(".","", 1).replace(",","")):
            return a
        else:
            return None
    else:
        return None

# Alternative Solution

def compare_one(a, b):
    if a == b:
        return None
    else: