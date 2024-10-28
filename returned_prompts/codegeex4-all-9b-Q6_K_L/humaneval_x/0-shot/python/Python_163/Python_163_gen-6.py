def generate_integers(a, b):
    return sorted(set(d for i in range(a, b + 1) for d in str(i) if int(d) % 2 == 0))

print(generate_integers(2, 8))  # [2, 4, 6, 8]
print(generate_integers(8, 2))  # [2, 4, 6, 8]
print(generate_integers(10, 14))  # []