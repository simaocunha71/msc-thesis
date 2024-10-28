def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    last_char = txt[-1]
    if last_char.isalpha() and not txt[-2:-1].isdigit():
        return True
    return False

print(check_if_last_char_is_a_letter("apple pie")) # ➞ False
print(check_if_last_char_is_a_letter("apple pi e")) # ➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) # ➞ False
print(check_if_last_char_is_a_letter("")) # ➞ False

# Explanation:
# The last character is 'e' which is alphabetical and not part of a word.
# The last character is ' ' which is not alphabetical.
# The last character is ' ' which is not alphabetical.
# The string is empty, so return False.