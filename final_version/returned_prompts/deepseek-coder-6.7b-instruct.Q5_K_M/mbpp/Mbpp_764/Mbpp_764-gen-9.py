def number_ctr(s):
    return sum(c.isdigit() for c in s)

# test
assert number_ctr('program2bedone') == 1

