    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x//base, base) + convertString[x%base]


