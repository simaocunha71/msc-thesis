def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())  # Check if the name starts with an uppercase letter