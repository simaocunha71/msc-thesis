
def check_none(tup):
    if None in tup:
        return True
    else:
        return False

print(check_none((10, 4, 5, 6, None)))  # Output: True
print(check_none((10, 4, 5, 6, )))  # Output: False


