def count_upper(s):
    vowels = 'AEIOU'
    return sum(1 for i in range(len(s)) if s[i] in vowels and i % 2 == 0)

print(count_upper('aBCdEf')) # returns 1
print(count_upper('abcdefg')) # returns 0
print(count_upper('dBBE')) # returns 0