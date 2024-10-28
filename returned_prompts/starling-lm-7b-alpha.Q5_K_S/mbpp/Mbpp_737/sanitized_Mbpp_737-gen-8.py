import re
def check_str(str):
    vowel = "aeiou"
    return bool(re.match(vowel, str))