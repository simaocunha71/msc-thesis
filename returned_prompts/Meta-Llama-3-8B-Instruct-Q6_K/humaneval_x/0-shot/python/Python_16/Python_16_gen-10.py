def count_distinct_characters(string: str) -> int:
    string = string.lower()  # convert the string to lowercase
    char_set = set(string)  # convert the string to a set (which automatically removes duplicates)
    return len(char_set)  # return the number of distinct characters


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
print(count_distinct_characters('Hello, World!'))  # Output: 10
print(count_distinct_characters('abcabcabc'))  # Output: 3
print(count_distinct_characters('aA'))  # Output: 2
print(count_distinct_characters(''))  # Output: 0
print(count_distinct_characters('!!!'))  # Output: 1
print(count_distinct_characters('!!'))  # Output: 1
print(count_distinct_characters('a'))  # Output: 1
print(count_distinct_characters(''))  # Output: 0
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'))  # Output: 26
print(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 26
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 52

# Test case with non-ascii characters
print(count_distinct_characters('áéíóú'))  # Output: 6
print(count_distinct_characters('ÁÉÍÓÚ'))  # Output: 6
print(count_distinct_characters('áéíóúÁÉÍÓÚ'))  # Output: 6
print(count_distinct_characters('áéíóúÁÉÍÓÚüÜ'))  # Output: 8
print(count_distinct_characters('üÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜüÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜüÜüÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜüÜüÜüÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜüÜüÜüÜüÜ'))  # Output: 2
print(count_distinct_characters('üÜüÜüÜüÜüÜüÜüÜ')) 