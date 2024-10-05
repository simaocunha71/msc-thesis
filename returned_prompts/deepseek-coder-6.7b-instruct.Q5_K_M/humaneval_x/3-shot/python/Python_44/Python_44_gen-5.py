    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)

# print(change_base(8, 3))
# print(change_base(8, 2))
# print(change_base(7, 2))

