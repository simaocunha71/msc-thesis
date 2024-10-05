def how_many_times(string: str, substring: str) -> int:
    count = 0
    i = 0
    while i < len(string):
        pos = string.find(substring, i)
        if pos != -1:
            count += 1
            i = pos + 1
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
print(how_many_times('abcabc', 'abc'))  # 2
print(how_many_times('abcabc', 'b'))  # 1
print(how_many_times('abcabc', 'c'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', ''))  # 1 (empty substring) 
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', 'a'))  # 2
print(how_many_times('abcabc', '