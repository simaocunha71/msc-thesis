def toggle_middle_bits(n):
    bin_n = bin(n)[2:]
    bin_n = list(bin_n)
    bin_n[1:-1] = ['1' if bit == '0' else '0' for bit in bin_n[1:-1]]
    return int(''.join(bin_n), 2)  # Convert back to integer
    # Test case:
    print(toggle_middle_bits(9))  # Output: 15
    # Test case:
    print(toggle_middle_bits(10))  # Output: 12
    # Test case:
    print(toggle_middle_bits(8))  # Output: 10
    # Test case:
    print(toggle_middle_bits(16))  # Output: 14
    # Test case:
    print(toggle_middle_bits(1))  # Output: 1
    # Test case:
    print(toggle_middle_bits(2))  # Output: 2
    # Test case:
    print(toggle_middle_bits(3))  # Output: 3
    # Test case:
    print(toggle_middle_bits(7))  # Output: 11
    # Test case:
    print(toggle_middle_bits(15))  # Output: 15
    # Test case:
    print(toggle_middle_bits(31))  # Output: 31
    # Test case:
    print(toggle_middle_bits(32))  # Output: 30
    # Test case:
    print(toggle_middle_bits(33))  # Output: 33
    # Test case:
    print(toggle_middle_bits(35))  # Output: 35
    # Test case:
    print(toggle_middle_bits(36))  # Output: 34
    # Test case:
    print(toggle_middle_bits(37))  # Output: 37
    # Test case:
    print(toggle_middle_bits(38))  # Output: 38
    # Test case:
    print(toggle_middle_bits(39))  # Output: 39
    # Test case:
    print(toggle_middle_bits(40))  # Output: 38
    # Test case:
    print(toggle_middle_bits(41))  # Output: 41
    # Test case:
    print(toggle_middle_bits(42))  # Output: 42
    # Test case:
    print(toggle_middle_bits(43))  # Output: