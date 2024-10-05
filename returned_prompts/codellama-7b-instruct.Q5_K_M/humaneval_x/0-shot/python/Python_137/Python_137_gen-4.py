
def compare_one(a, b):
    if str(a) == str(b):
        return None
    elif float(a) > float(b):
        return a
    else:
        return b
