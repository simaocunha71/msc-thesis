def is_url(s):
    return bool(re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[^\s])*', s))

print(is_url("python"))  # False
print(is_url("https://www.google.com"))  # True

"""
Write