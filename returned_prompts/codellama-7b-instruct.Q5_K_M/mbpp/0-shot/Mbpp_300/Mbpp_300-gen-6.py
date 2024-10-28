def count_binary_seq(n):
    count = 0
    for i in range(1<<n):
        if sum(bin(i)[2:].zfill(n)[::-1]) == sum(bin(i)[2:].zfill(n)):
            count += 1
    return count

# Tests
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(2), 4.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(3), 8.0, rel_tol=0.001)
assert math.isclose(count_binary_seq(4), 16.0, rel_tol=0.001)

# Code
def count_binary_seq(n):
    count = 0
    for i in range(1<<n):
        if sum(bin(i)[2:].zfill(n)[::-1]) == sum(bin(i)[2:].zfill(n)):
            count += 1
    return count
