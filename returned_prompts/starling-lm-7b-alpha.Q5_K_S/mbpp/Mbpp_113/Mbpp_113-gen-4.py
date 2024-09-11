"""
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
"""

def check_integer(s):
    return s.isdigit()


print(check_integer("python"))
print(check_integer("123"))

# 123 -> True
# python -> False

# 0123 -> True
# 0123a -> False

# 123.45 -> False
# 12345 -> True

# -123 -> True
# -123a -> False

# 123abc -> False
# abc123 -> False

# 1234567890123456789 -> True
# 12345678901234567890 -> False

# 123.45 -> False
# 12345 -> True

# -123 -> True
# -123a -> False

# 123abc -> False
# abc123 -> False

# 1234567890123456789 -> True
# 12345678901234567890 -> False

# 123.45 -> False
# 12345 -> True

# -123 -> True
# -123a -> False

# 123abc -> False
# abc123 -> False

# 1234567890123456789 -> True
# 12345678901234567890 -> False

# 123.45 -> False
# 12345 -> True

# -123 -> True
# -123a -> False

# 123abc -> False
# abc123 -> False

# 123456789012345678