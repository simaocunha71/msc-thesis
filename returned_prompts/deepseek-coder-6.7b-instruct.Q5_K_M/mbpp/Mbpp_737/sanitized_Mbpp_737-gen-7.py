def check_str(s):
    pattern = "^[aeiou]"
    if re.match(pattern, s):
        return True
    else:
        return False