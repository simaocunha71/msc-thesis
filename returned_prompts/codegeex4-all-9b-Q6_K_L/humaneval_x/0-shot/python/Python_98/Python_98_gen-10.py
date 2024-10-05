def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = set('AEIOU')
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)

print(count_upper('aBCdEf')) # returns 1
print(count_upper('abcdefg')) # returns 0
print(count_upper('dBBE')) # returns 0