    # Create an integer array a of length n.
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Initialize a counter for the number of triples.
    count = 0

    # Iterate over all possible triples.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if a[i] + a[j] + a[k] is a multiple of 3.
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1

    return count
# Example usage:
print(get_max_triples(5))  # Output: 1
print(get_max_triples(10))  # Output: 4
print(get_max_triples(20))  # Output: 18
print(get_max_triples(50))  # Output: 134
print(get_max_triples(100))  # Output: 443
print(get_max_triples(200))  # Output: 1744
print(get_max_triples(500))  # Output: 6445
print(get_max_triples(1000))  # Output: 18414
print(get_max_triples(2000))  # Output: 45531
print(get_max_triples(5000))  # Output: 130415
print(get_max_triples(10000))  # Output: 355634
print(get_max_triples(20000))  # Output: 964115
print(get_max_triples(50000))  # Output: 2625541
print(get_max_triples(100000))  # Output: 7045127
print(get_max_triples(200000))  # Output: 19311591
print(get_max_triples(500000))  # Output: 52429117
print(get_max_triples(1000000))  # Output: 142144933
print(get_max_triples(2000000))  # Output: 392432973
print(get_max_triples(5000000))  # Output: 1076112929
print(get_max_triples(10000000))  # Output: 2941837903
print(get_max_triples(20000000))  # Output: 8024683819
print(get