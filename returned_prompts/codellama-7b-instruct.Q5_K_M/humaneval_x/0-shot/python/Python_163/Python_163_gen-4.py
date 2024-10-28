
def generate_integers(a, b):
    return sorted([x for x in range(a, b+1) if x % 2 == 0])
