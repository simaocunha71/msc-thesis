def decimal_to_binary(n):
    return bin(n).replace("0b", "")

print(decimal_to_binary(8))  # Should print 1000


# Second solution using recursion
def decimal_to_binary_rec(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_to_binary_rec(n // 2) + str(n % 2)

print(decimal_to_binary_rec(8))  # Should print 1000


# Third solution using stack
def decimal_to_binary_stack(n):
    stack = []

    while n > 0:
        stack.append(str(n % 2))
        n = n // 2

    return ''.join(reversed(stack))

print(decimal_to_binary_stack(8))  # Should print 1000


# Fourth solution using bitwise operators
def decimal_to_binary_bitwise(n):
    binary = []

    while n > 0:
        binary.insert(0, str(n & 1))
        n = n >> 1

    return ''.join(binary)

print(decimal_to_binary_bitwise(8))  # Should print 1000


# Fifth solution using format function
def decimal_to_binary_format(n):
    return "{0:b}".format(n)

print(decimal_to_binary_format(8))  # Should print 1000


# Sixth solution using f-string
def decimal_to_binary_fstring(n):
    return f"{n:b}"

print(decimal_to_binary_fstring(8))  # Should print 1000


# Seventh solution using list comprehension
def decimal_to_binary_comprehension(n):
    return ''.join([str(n >> i & 1) for i in range(n.bit_length() - 1, -1, -