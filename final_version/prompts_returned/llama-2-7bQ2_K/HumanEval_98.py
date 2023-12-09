
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    n = len(s)
    cnt = 0
    
    for x in range(n, -1, -2):
        if s[x].isupper() and s[x:len(s)].count('A'*2 + 'B') == 0:
            cnt += 1
            
    return cnt