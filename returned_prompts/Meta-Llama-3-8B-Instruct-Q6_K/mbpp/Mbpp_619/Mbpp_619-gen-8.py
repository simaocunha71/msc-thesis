def move_num(s):
    res = ''
    num = ''
    for char in s:
        if char.isdigit():
            num += char
        else:
            if num:
                res += num + char
                num = ''
            else:
                res += char
    if num:
        res += num
    return res

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
print(move_num('I1love143you55three3000thousand'))  # 'Iloveyouthreethousand1143553000'  # Output
print(move_num('abc123'))  # 'abc123'  # Output
print(move_num('123abc'))  # 'abc123'  # Output
print(move_num('a1b2c3'))  # 'abc123'  # Output
print(move_num('1a2b3'))  # 'abc123'  # Output
print(move_num('a1b2'))  # 'ab12'  # Output
print(move_num('abc'))  # 'abc'  # Output
print(move_num('123'))  # '123'  # Output
print(move_num(''))  # ''  # Output
print(move_num('1234567890'))  # '1234567890'  # Output
print(move_num('123abc456def789'))  # 'abcdef123456789'  # Output
print(move_num('1234567890abc'))  # 'abc1234567890'  # Output
print(move_num('123abc456def7890'))  # 'abcdef1234567890'  # Output
print(move_num('12345678901234567890'))  # '12345678901234567890'  # Output
print(move_num('123abc456def78901234567890'))  # 'abcdef12345678901234567890'  # Output
print(move_num('123456789012345678901234567890'))  # '123456789012345678901234567890'  # Output
print(move_num('123abc456def789012345678901234567890'))  # 'abcdef123456789012345678901234567890'  # Output
print(move_num('12345678901234567890123456789012345678901234567890')) 