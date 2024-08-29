def remove_all(s, sub):
    return s.replace(sub, '')

print(remove_all("This is a test string. This is only a test.", "is"))

"""
Write a function to remove all duplicate characters from a string.
assert remove_duplicates("This is a test string.")==("T