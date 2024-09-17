def check_str(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if re.match('^[aeiouAEIOU]', s):
        return True
    else:
        return False