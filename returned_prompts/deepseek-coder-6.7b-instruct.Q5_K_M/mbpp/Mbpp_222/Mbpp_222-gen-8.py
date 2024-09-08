def check_type(t):
    return len(set(map(type, t))) <= 1

assert check_type((5, 6, 7, 3, 5, 6)) == True

# Alternative solution
def check_type(t):
    return all(isinstance(i, type(t[0])) for i in t)

assert check_type((5, 6, 7, 3, 5, 6)) == True

