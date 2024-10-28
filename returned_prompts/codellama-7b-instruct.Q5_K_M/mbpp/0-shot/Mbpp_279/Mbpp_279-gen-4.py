def is_num_decagonal(n):
    if n < 3:
        return False
    return ((n - 3) * 2) % 3 == 0

def find_nth_decagonal_num(n):
    if n < 3:
        raise ValueError("Invalid input: n should be greater than 2")
    if is_num_decagonal(n):
        return n
    else:
        for i in range(3, n):
            if is_num_decagonal(i):
                return i
        return None

# Tests
assert find_nth_decagonal_num(3) == 27
assert find_nth_decagonal_num(4) == 42
assert find_nth_decagonal_num(5) == 55
