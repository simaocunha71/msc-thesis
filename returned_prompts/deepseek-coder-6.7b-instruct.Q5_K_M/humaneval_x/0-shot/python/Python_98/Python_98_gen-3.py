
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

print(count_upper('aBCdEf')) # 1
print(count_upper('abcdefg')) # 0
print(count_upper('dBBE')) # 0
print(count_upper('ABCDE')) # 2
print(count_upper('ABCD')) # 1
print(count_upper('aBcDe')) # 1
print(count_upper('AbCdE')) # 1
print(count_upper('ABCdE')) # 1
print(count_upper('aBcD')) # 0
print(count_upper('AbCd')) # 0
print(count_upper('ABCD')) # 0
print(count_upper('ABCDE')) # 0
print(count_upper('ABCDEF')) # 0
print(count_upper('aBcDeF')) # 1
print(count_upper('AbCdEf')) # 1
print(count_upper('ABCdEF')) # 0
print(count_upper('ABCD')) # 0
print(count_upper('ABCDE')) # 0
print(count_upper('ABCDEF')) # 0
print(count_upper('aBcDeFg')) # 1
print(count_upper('AbCdEfG')) # 1
print(count_upper('ABCdEFG')) # 0
print(count_upper('ABCDEFG')) # 0
print(count_upper('ABCD')) # 0
print(count_upper('ABCDE')) # 0
print(count_upper('ABCDEF')) # 0
print(count_upper('ABCDEFG')) # 0
print(count_upper('ABCDEFGH')) # 0
print(count_upper('ABCDEFGHI')) # 0
print(count_upper('ABCDEFGHIJ')) # 0
print(count_upper('ABCDEFGHIJK')) # 0