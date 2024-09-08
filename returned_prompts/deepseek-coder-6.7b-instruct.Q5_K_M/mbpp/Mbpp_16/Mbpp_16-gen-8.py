def text_lowercase_underscore(text):
    words = text.split("_")
    for word in words:
        if not word.islower():
            return False
    return True

print(text_lowercase_underscore("aab_cbbbc"))  # should return True

