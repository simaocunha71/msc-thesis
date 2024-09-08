def remove_lowercase(s):
    return "".join([i for i in s if i.isupper()])

assert remove_lowercase("PYTHon")==('PYTH')


