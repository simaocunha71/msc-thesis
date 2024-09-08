def remove_dirty_chars(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1

print(remove_dirty_chars("probasscurve", "pros"))

# Output: 'bacuve'

# ---------

