    if type(a) == int and type(b) == int:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == int and type(b) == float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == float and type(b) == int:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == float and type(b) == float:
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif type(a) == str and type(b) == str:
        if float(a.replace(',', '.')) > float(b.replace(',', '.')):
            return a
        elif float(a.replace(',', '.')) < float(b.replace(',', '.')):
            return b
        else:
            return None
    else:
        return None


