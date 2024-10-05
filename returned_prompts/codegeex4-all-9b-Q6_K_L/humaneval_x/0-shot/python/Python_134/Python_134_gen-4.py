def check_if_last_char_is_a_letter(txt):
    return txt and not txt[-1].isalpha() and txt[-1].strip() == txt[-1]

print(check_if_last_char_is_a_letter("apple pie")) #➞ False
print(check_if_last_char_is_a_letter("apple pi e")) #➞ True
print(check_if_last_char_is_a_letter("apple pi e ")) #➞ False
print(check_if_last_char_is_a_letter("")) #➞ False 

# Explanation:
# txt[-1] returns the last character of the string.
# txt[-1].isalpha() checks if the last character is a letter.
# txt[-1].strip() == txt[-1] checks if the last character is not a part of a word.