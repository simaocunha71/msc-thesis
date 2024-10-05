
def tri(n):
    # The first two numbers are fixed
    tri_seq = [3, 1]
    # If n is 0, return the initial sequence
    if n == 0:
        return tri_seq
    # If n is 1, append the next number in the sequence and return
    if n == 1:
        tri_seq.append(2)
        return tri_seq
    # If n is 2, append the next two numbers in the sequence and return
    if n == 2:
        tri_seq.append(8)
        return tri_seq
    # If n is odd, add the next three numbers in the sequence
    if n % 2 != 0:
        for i in range(3, n + 1):
            if i % 2 != 0:
                tri_seq.append(tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i + 1])
            else:
                tri_seq.append(1 + i / 2)
    # If n is even, add the next two numbers in the sequence
    if n % 2 == 0:
        for i in range(3, n + 1):
            if i % 2 == 0:
                tri_seq.append(1 + i / 2)
            else:
                tri_seq.append(tri_seq[i - 1] + tri_seq[i - 2] + tri_seq[i + 1])
    return tri_seq

# Test the function
print(tri(3))  # [1, 3, 2, 8]
print(tri(4))  # [1, 3, 1, 8]
print(tri(2))  # [1, 3, 8]
















































































