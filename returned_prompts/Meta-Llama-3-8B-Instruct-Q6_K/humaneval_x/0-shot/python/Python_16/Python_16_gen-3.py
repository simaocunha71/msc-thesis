def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
# The set function will automatically remove duplicate characters, and the lower() function will convert the string to lowercase to make it case-insensitive. The length of the set will be the number of distinct characters.

# Test cases:
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
print(count_distinct_characters('HelloWorld'))  # Expected output: 10
print(count_distinct_characters('PythonProgramming'))  # Expected output: 13
print(count_distinct_characters(''))  # Expected output: 0
print(count_distinct_characters('a'))  # Expected output: 1
print(count_distinct_characters('aaa'))  # Expected output: 1
print(count_distinct_characters('abcdefg'))  # Expected output: 7
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'))  # Expected output: 26
print(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Expected output: 26
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Expected output: 52
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))  # Expected output: 62
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}:<>?,./;[]\\|`~'))  # Expected output: 95
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}:<>?,./;[]\\|`~[]{};':",.<>/?\\|!@#$%^&*()_+-={}[]|;:`~'))  # Expected output: 95
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}:<>?,./;[]\\|`~[]{};':",.<>/?\\|!@#$%^&*()_+-={}[]|;:`~[]{};':",.<>/?\\|!@#$%^&*()_+-={}[]|;:`~'))  # Expected output: 95
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}:<>?,./;[]\\|`~[]{};':",.<>/?\\|!@#$%^&*()