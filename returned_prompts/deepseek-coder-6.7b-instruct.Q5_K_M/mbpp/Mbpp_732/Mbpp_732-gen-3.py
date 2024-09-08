def replace_specialchar(s):
    for char in s:
        if char in " ,.":
            s = s.replace(char, ":")
    return s

print(replace_specialchar('Python language, Programming language.'))

# Output:
# Python:language::Programming:language:

# Solution 2:
