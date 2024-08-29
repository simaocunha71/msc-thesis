
def first_repeated_char(string):
    visited_chars = set()
    for char in string:
        if char in visited_chars:
            return char
        visited_chars.add(char)
    return None

print(first_repeated_char("abcabc"))  # "a"

# 1. The function iterates over the characters in the input string.
# 2. It keeps track of the characters it has visited so far in a set.
# 3. If it encounters a character that is already in the set, it returns that character.
# 4. If it does not encounter a repeated character before it finishes iterating over the string, it returns None.


# 2nd method
def first_repeated_char(string):
    counts = {}
    for char in string:
        if char in counts:
            return char
        counts[char] = 1
    return None

print(first_repeated_char("abcabc"))  # "a"

# 1. The function iterates over the characters in the input string.
# 2. It keeps track of the count of each character it has seen so far in a dictionary.
# 3. If it encounters a character that is already in the dictionary, it returns that character.
# 4. If it does not encounter a repeated character before it finishes iterating over the string, it returns None.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
