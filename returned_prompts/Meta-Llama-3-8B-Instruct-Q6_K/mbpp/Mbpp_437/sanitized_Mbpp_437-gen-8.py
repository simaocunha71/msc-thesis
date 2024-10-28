def remove_odd(s):
    return "".join([c for c in s if int(c) % 2 == 0 or not c.isdigit()])  # or not c.isdigit() for alphanumeric characters