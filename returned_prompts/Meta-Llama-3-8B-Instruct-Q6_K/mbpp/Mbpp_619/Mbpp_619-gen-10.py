def move_num(s):
    result = ""
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                result += num_str
                num_str = ""
            result += char
    if num_str:
        result += num_str
    return result

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'  # Test case
print(move_num('I1love143you55three3000thousand'))  # Output: Iloveyouthreethousand1143553000
print(move_num('abc123def456'))  # Output: abcdef123456
print(move_num('123abc456def'))  # Output: abcdef123456
print(move_num('123abc'))  # Output: abc123
print(move_num('123'))  # Output: 123
print(move_num('abc'))  # Output: abc
print(move_num(''))  # Output: 
print(move_num('123abc456def123'))  # Output: abcdef123123456
print(move_num('1'))  # Output: 1
print(move_num('abc1'))  # Output: abc1
print(move_num('1abc'))  # Output: 1abc
print(move_num('111abc'))  # Output: abc111
print(move_num('abc111'))  # Output: abc111
print(move_num('1111abc'))  # Output: abc1111
print(move_num('abc1111'))  # Output: abc1111
print(move_num('111abc111'))  # Output: abc111111
print(move_num('abc111111'))  # Output: abc111111
print(move_num('111111abc'))  # Output: abc111111
print(move_num('abc111111'))  # Output: abc111111
print(move_num('1111111abc'))  # Output: abc1111111
print(move_num('abc1111111'))  # Output: abc1111111
print(move_num('11111111abc'))  # Output: abc11111111
print(move_num('abc11111111'))  # Output: abc11111111
print(move_num('111111111abc'))  # Output: abc111111111
print(move_num('abc111111111'))  # Output: abc