    return 0.5 * a * h
    # Test cases:
    print(triangle_area(5, 3))  # Expected output: 7.5
    print(triangle_area(10, 4))  # Expected output: 20.0
    print(triangle_area(3, 2))  # Expected output: 3.0
    # Test the function with negative values:
    print(triangle_area(-5, 3))  # Expected output: -7.5
    print(triangle_area(5, -3))  # Expected output: -7.5
    print(triangle_area(-5, -3))  # Expected output: 7.5
    print(triangle_area(0, 3))  # Expected output: 0.0
    print(triangle_area(5, 0))  # Expected output: 0.0
    print(triangle_area(0, 0))  # Expected output: 0.0

    # Test the function with non-numeric inputs:
    print(triangle_area("a", 3))  # Expected output: TypeError
    print(triangle_area(5, "b"))  # Expected output: TypeError
    print(triangle_area("a", "b"))  # Expected output: TypeError
    print(triangle_area(None, 3))  # Expected output: TypeError
    print(triangle_area(5, None))  # Expected output: TypeError
    print(triangle_area(None, None))  # Expected output: TypeError

    # Test the function with complex numbers:
    print(triangle_area(5 + 3j, 3))  # Expected output: 7.5 + 0j
    print(triangle_area(10 + 4j, 4))  # Expected output: 20.0 + 0j
    print(triangle_area(3 + 2j, 2))  # Expected output: 3.0 + 0j
    print(triangle_area(-5 + 3j, 3))  # Expected output: -7.5 + 0j
    print(triangle_area(5 + 3j, -3))  # Expected output: -7.5 + 0j
    print(triangle_area(-5 + 3j, -3))  # Expected output: 7.5 + 0j
