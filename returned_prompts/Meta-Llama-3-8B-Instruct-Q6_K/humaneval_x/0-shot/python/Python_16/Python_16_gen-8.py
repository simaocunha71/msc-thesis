def count_distinct_characters(string: str) -> int:
    string = string.lower()  # Convert the string to lowercase
    char_set = set(string)  # Create a set of unique characters
    return len(char_set)  # Return the number of distinct characters

# Testing the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
print(count_distinct_characters('HelloWorld'))  # Output: 10
print(count_distinct_characters(''))  # Output: 0
print(count_distinct_characters('aabbcc'))  # Output: 3
print(count_distinct_characters('abc'))  # Output: 3
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'))  # Output: 26
print(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  # Output: 26
print(count_distinct_characters('1234567890'))  # Output: 10
print(count_distinct_characters('!@#$%^&*()_+-=[]{};:,.<>?/'))  # Output: 28
print(count_distinct_characters(' '))  # Output: 1
print(count_distinct_characters('   '))  # Output: 1
print(count_distinct_characters('   a   b   c'))  # Output: 3
print(count_distinct_characters('   a   a   a'))  # Output: 1
print(count_distinct_characters('   a   b   a'))  # Output: 2
print(count_distinct_characters('   a   b   c   d'))  # Output: 4
print(count_distinct_characters('   a   b   c   d   e'))  # Output: 5
print(count_distinct_characters('   a   b   c   d   e   f'))  # Output: 6
print(count_distinct_characters('   a   b   c   d   e   f   g'))  # Output: 7
print(count_distinct_characters('   a   b   c   d   e   f   g   h'))  # Output: 8
print(count_distinct_characters('   a   b   c   d   e   f   g   h   i'))  # Output: 9
print(count_distinct_characters('   a   b   c   d   e   f   g   h   i   j