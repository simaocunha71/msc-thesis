
def find_length(s):
    s = s + '0'
    max_len = 0
    for i in range(len(s)-1):
        if s[i] == '0':
            max_len = max(max_len, (s.rfind('1', 0, i+1) - s.find('0', 0, i+1)) + 1)
    return max_len


