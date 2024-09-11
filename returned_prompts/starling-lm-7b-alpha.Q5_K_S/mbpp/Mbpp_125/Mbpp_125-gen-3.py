"""
def find_length(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            zero_count = s[i:j].count('0')
            one_count = s[i:j].count('1')
            max_length = max(max_length, abs(zero_count - one_count))
    return max_length

print(find_length("11000010001"))
"""

def find_length(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            zero_count = s[i:j].count('0')
            one_count = s[i:j].count('1')
            max_length = max(max_length, abs(zero_count - one_count))
    return max_length

print(find_length("11000010001"))



def find_length(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            zero_count = s[i:j].count('0')
            one_count = s[i:j].count('1')
            max_length = max(max_length, abs(zero_count - one_count))
    return max_length

print(find_length("11000010001"))



def find_length(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            zero_count = s[i:j].count('0')
            one_count = s[i:j].count('1')
            max_length = max(max_length, abs(zero_count - one_count))
    return max_length

print(find_length("11000010001"))



def find