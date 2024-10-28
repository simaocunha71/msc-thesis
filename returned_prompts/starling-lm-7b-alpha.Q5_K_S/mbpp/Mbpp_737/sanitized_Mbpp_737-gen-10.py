def check_str(string):
    vowels = "[aeiou]"
    if re.match(vowels, string[0]):
        return True
    else:
        return False