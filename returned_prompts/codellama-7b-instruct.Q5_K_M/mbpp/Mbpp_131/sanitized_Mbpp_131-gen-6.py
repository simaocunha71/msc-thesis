import re
def reverse_vowels(input_string):
    vowels = re.findall(r"[aeiou]", input_string)
    vowels.reverse()
    for i, vowel in enumerate(vowels):
        input_string = input_string.replace(vowel, "", 1)
        input_string = vowel + input_string
    return input_string