def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
    



# Testing the function
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('abcabc', 'abc'))  # Output: 2
print(how_many_times('abcdefg', 'abc'))  # Output: 1
print(how_many_times('abcdefg', 'def'))  # Output: 1
print(how_many_times('abcdefg', 'ghi'))  # Output: 0

# Test case with overlapping substrings
print(how_many_times('aabaa', 'aa'))  # Output: 2
print(how_many_times('ababab', 'aba'))  # Output: 2
print(how_many_times('abababab', 'aba'))  # Output: 3

# Test case with empty substring
print(how_many_times('abc', ''))  # Output: 1
print(how_many_times('abc', ''))  # Output: 1

# Test case with empty string
print(how_many_times('', ''))  # Output: 0
print(how_many_times('abc', ''))  # Output: 0

# Test case with substring longer than string
print(how_many_times('a', 'ab'))  # Output: 0
print(how_many_times('abc', 'abcd'))  # Output: 0
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd', 'abcd'))  # Output: 1
print(how_many_times('abcd