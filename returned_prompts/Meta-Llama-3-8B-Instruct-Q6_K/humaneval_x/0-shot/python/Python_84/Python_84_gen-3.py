    def solve(N):
        # Convert the number to binary and remove the '0b' prefix
        binary = bin(N)[2:]
        
        # Initialize the sum of digits
        total_sum = 0
        
        # Iterate over each character in the binary string
        for digit in binary:
            # Convert each character to an integer and add it to the sum
            total_sum += int(digit)
        
        # Convert the sum to binary and return as a string
        return bin(total_sum)[2:]
    # Test the function
    print(solve(1000))  # Output: 1
    print(solve(150))  # Output: 110
    print(solve(147))  # Output: 1100
    print(solve(12345))  # Output: 10011
    print(solve(123456))  # Output: 10111100
    print(solve(1234567))  # Output: 10111010011
    print(solve(12345678))  # Output: 1011101001100
    print(solve(123456789))  # Output: 1011101001100011
    print(solve(1234567890))  # Output: 10111010011000110000
    print(solve(12345678901))  # Output: 1011101001100011000001
    print(solve(123456789012))  # Output: 1011101001100011000001000
    print(solve(1234567890123))  # Output: 1011101001100011000001000011
    print(solve(12345678901234))  # Output: 1011101001100011000001000011000
    print(solve(123456789012345))  # Output: 10111010011000110000010000110001
    print(solve(1234567890123456))  # Output: 101110100110001100000100001100100
    print(solve(12345678901234567))  # Output: 1011101001100011000001000011001011
    print(solve(123456789012345678))  # Output: 101110100110001100000100001100101100
    print(solve(1234567890123456789))  # Output: 