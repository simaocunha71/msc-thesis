    count = 0
    upper_case = ['A', 'E', 'I', 'O', 'U']
    for i in range(0, len(s), 2):
        if s[i] in upper_case:
            count += 1
    return count


# Test cases
print(count_upper('aBCdEf'))  # 1
print(count_upper('abcdefg'))  # 0
print(count_upper('dBBE'))  # 0


# My answer:
def count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in ['A', 'E', 'I', 'O', 'U']:
            count += 1
    return count


# Test cases
print(count_upper('aBCdEf'))  # 1
print(count_upper('abcdefg'))  # 0
print(count_upper('dBBE'))  # 0


# My answer:
def count_upper(s):
    count = 0
    upper_case = ['A', 'E', 'I', 'O', 'U']
    for i in range(0, len(s), 2):
        if s[i] in upper_case:
            count += 1
    return count


# Test cases
print(count_upper('aBCdEf'))  # 1
print(count_upper('abcdefg'))  # 0
print(count_upper('dBBE'))  # 0

# Another solution:
def count_upper(s):
    return sum(1 for i, c in enumerate(s) if i % 2 == 0 and c.upper() in ['A', 'E', 'I', 'O', 'U'])


# Test cases
print(count_upper('aBCdEf'))  # 1
print(count_upper('abcdefg'))  # 0
print(count_upper('dBBE'))  # 0


# Another solution:
def count_upper(s):
    return sum(c.isupper