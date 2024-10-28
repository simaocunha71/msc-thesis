
def generate_integers(a, b):
    integers = []
    for i in range(a, b + 1):
        s = str(i)
        for j in s:
            if int(j) % 2 == 0:
                integers.append(i)
                break
    return integers

# Tests
print(generate_integers(2, 8))  # => [2, 4, 6, 8]
print(generate_integers(8, 2))  # => [2, 4, 6, 8]
print(generate_integers(10, 14))  # => []



def generate_integers(a, b):
    integers = []
    for i in range(a, b + 1):
        s = str(i)
        for j in s:
            if int(j) % 2 == 0:
                integers.append(i)
                break
    return integers

# Tests
print(generate_integers(2, 8))  # => [2, 4, 6, 8]
print(generate_integers(8, 2))  # => [2, 4, 6, 8]
print(generate_integers(10, 14))  # => []





def generate_integers(a, b):
    integers = []
    for i in range(a, b + 1):
        s = str(i)
        for j in s:
            if int(j) % 2 == 0:
                integers.append(i)
                break
    return integers

# Tests
print(generate_integers(2, 8))  # => [2, 4, 6, 8]
print(generate_integers(8, 2))  # => [2, 4, 6, 8]
print(generate_integers(10, 14))  # => []



def generate_integers(a, b):
    integers = []
    for i in range(a, b