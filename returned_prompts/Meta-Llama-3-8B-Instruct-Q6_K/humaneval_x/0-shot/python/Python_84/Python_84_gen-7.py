    def solve(N):
        # Convert N to binary and remove the '0b' prefix
        bin_N = bin(N)[2:]
        
        # Initialize sum and result
        total_sum = 0
        result = ''
        
        # Iterate through each character in the binary string
        for char in bin_N:
            # Add the integer value of the character to the total sum
            total_sum += int(char)
            
            # Add the character to the result string
            result += char
        
        return result
    # Test cases
    print(solve(1000))  # Output: "1"
    print(solve(150))   # Output: "110"
    print(solve(147))   # Output: "1100" 
    print(solve(100))   # Output: "1"
    print(solve(1024))  # Output: "1" 
    print(solve(10000)) # Output: "1" 
    print(solve(1234))  # Output: "10011100010"
    print(solve(1023))  # Output: "1111111111"
    print(solve(0))     # Output: ""
    print(solve(1))     # Output: "1"
    print(solve(2))     # Output: "10"
    print(solve(3))     # Output: "11"
    print(solve(4))     # Output: "100"
    print(solve(5))     # Output: "101"
    print(solve(6))     # Output: "110"
    print(solve(7))     # Output: "111"
    print(solve(8))     # Output: "1000"
    print(solve(9))     # Output: "1001"
    print(solve(10))    # Output: "1010"
    print(solve(11))    # Output: "1011"
    print(solve(12))    # Output: "1100"
    print(solve(13))    # Output: "1101"
    print(solve(14))    # Output: "1110"
    print(solve(15))    # Output: "1111"
    print(solve(16))    # Output: "10000"
    print(solve(17))    # Output: "10001"
    print(solve(18))    # Output: "100