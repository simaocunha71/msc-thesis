def find_Max_Num(digits):
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))  # convert to string and join, then convert back to int