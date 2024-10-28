
def generate_integers(a, b):
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 0:
        return [a] + generate_integers(a + 2, b)
    return generate_integers(a + 2, b)

# Test
print(generate_integers(2, 8)) # [2, 4, 6, 8]
print(generate_integers(8, 2)) # [2, 4, 6, 8]
print(generate_integers(10, 14)) # []





def generate_integers(a, b):
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 0:
        return [a] + generate_integers(a + 2, b)
    return generate_integers(a + 2, b)

# Test
print(generate_integers(2, 8)) # [2, 4, 6, 8]
print(generate_integers(8, 2)) # [2, 4, 6, 8]
print(generate_integers(10, 14)) # []





def generate_integers(a, b):
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 0:
        return [a] + generate_integers(a + 2, b)
    return generate_integers(a + 2, b)

# Test
print(generate_integers(2, 8)) # [2, 4, 6, 8]
print(generate_integers(8, 2)) # [2, 4, 6, 8]
print(generate_integers(10, 14)) # []





def generate_integers(a, b):
    if a > b:
        return generate_integers(b, a)
    if a % 2 == 0:
        return [a] + generate_integers(