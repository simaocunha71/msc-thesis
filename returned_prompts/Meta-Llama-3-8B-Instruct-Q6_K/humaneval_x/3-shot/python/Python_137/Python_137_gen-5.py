    def compare(a, b):
        if type(a) == int and type(b) == int:
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
        elif type(a) == int and type(b) == float:
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
        elif type(a) == float and type(b) == str:
            if a > float(b.replace(',', '.')):
                return a
            elif a < float(b.replace(',', '.')):
                return b
            else:
                return None
        elif type(a) == str and type(b) == int:
            if float(a.replace(',', '.')) > b:
                return a
            elif float(a.replace(',', '.')) < b:
                return b
            else:
                return None

    return compare(a, b)


