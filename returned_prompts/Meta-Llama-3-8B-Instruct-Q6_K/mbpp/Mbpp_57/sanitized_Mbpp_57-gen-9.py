def find_Max_Num(digits):
    return int(''.join(sorted(map(str, digits), reverse=True)))  # convert to string, sort and join back to string, then convert back to int