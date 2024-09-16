def is_num_decagonal(n):
    return ((2*n)**2 + (3*n)**2) % 4 == 0

def find_nth_decagonal(n):
    for i in range(1, n+1):
        if is_num_decagonal(i):
            return i

print(find_nth_decagonal(3))
