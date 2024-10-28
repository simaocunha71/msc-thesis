def move_num(s):
    num_str = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                s = s.replace(num_str, '', 1)
                s += num_str
                num_str = ''
    return s
print(move_num('I1love143you55three3000thousand')) # Iloveyouthreethousand1143553000
print(move_num('abc123def456')) # abcdef123456
print(move_num('123abc')) # abc123
print(move_num('123456')) # 123456
print(move_num('abc456')) # abc456
print(move_num('')) # 
print(move_num('abc')) # abc
print(move_num('123')) # 123
print(move_num('123abc456')) # abc456123
print(move_num('abc123def456')) # abcdef456123
print(move_num('123456789')) # 123456789
print(move_num('abc123def456ghi789')) # abcdefghi789123456
print(move_num('1234567890')) # 1234567890
print(move_num('abc123def456ghi789jkl')) # abcdefghi789jkl123456
print(move_num('1234567890abc')) # 1234567890abc
print(move_num('abc123def456ghi789jklm')) # abcdefghi789jklm123456
print(move_num('1234567890abc123')) # 1234567890abc123
print(move_num('abc123def456ghi789jklmno')) # abcdefghi789jklmno123456
print(move_num('1234567890abc123def456')) # 1234567890abc123def456
print(move_num('abc123def456ghi789jklmno123')) # abcdefghi789jklmno123456
print(move_num('1234567890abc123def456ghi789jklmno')) # 1234567890abc123def456ghi789jklmno
print(move_num('abc123def456ghi789jklmno123456')) # abcdefghi789jklmno1234567890
print(move_num('1234567890abc123def456ghi789jklmno123')) # 1234567890abc123def456ghi789jklmno123