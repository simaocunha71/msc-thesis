def is_valid_phone_number(num):
    if len(str(num)) != 10:
        return False
    if str(num)[0] == '0':
        return False
    if str(num)[1] == '0':
        return False
    if str(num)[2] == '0':
        return False
    if str(num)[3] == '0':
        return False
    if str(num)[4] == '0':
        return False
    if str(num)[5] == '0':
        return False
    if str(num)[6] == '0':
        return False
    if str(num)[7] == '0':
        return False
    if str(num)[8] == '0':
        return False
    if str(num)[9] == '0':
        return False
    return True

# assert is_valid_phone_number(234)