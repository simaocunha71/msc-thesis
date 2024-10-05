
def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False
print(prime_length('a'))  # False
print(prime_length('ab'))  # True
print(prime_length('abc'))  # False
print(prime_length('abcd'))  # False
print(prime_length('abcde'))  # True
print(prime_length('abcdef'))  # True
print(prime_length('abcdefg'))  # False
print(prime_length('abcdefgh'))  # False
print(prime_length('abcdefghi'))  # False
print(prime_length('abcdefghij'))  # True
print(prime_length('abcdefghijk'))  # False
print(prime_length('abcdefghijkl'))  # True
print(prime_length('abcdefghijklm'))  # False
print(prime_length('abcdefghijklmn'))  # False
print(prime_length('abcdefghijklmno'))  # False
print(prime_length('abcdefghijklmnop'))  # False
print(prime_length('abcdefghijklmnopq'))  # False
print(prime_length('abcdefghijklmnopqr'))  # False
print(prime_length('abcdefghijklmnopqrs'))  # False
print(prime_length('abcdefghijklmnopqrst'))  # False
print(prime_length('abcdefghijklmnopqrstu'))  # False
print(prime_length('abcdefghijklmnopqrstuv'))  # False
print(prime_length('abcdefghijklmnopqrstuvw'))  # False
print(prime_length('abcdefghijkl